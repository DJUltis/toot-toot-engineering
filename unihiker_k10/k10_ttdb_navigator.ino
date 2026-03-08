#include "unihiker_k10.h"
#include <SD.h>
#include <SPI.h>

UNIHIKER_K10 k10;
Music music;

const uint8_t SCREEN_DIR = 2;
const char *TTDB_PATH = "/ttdb_dice_k10.md";

const uint32_t COLOR_BG = 0x000000;
const uint32_t COLOR_TEXT = 0x00FF66;
const uint32_t COLOR_MUTED = 0x2E7D32;
const uint32_t COLOR_ACCENT = 0x00E676;
const uint32_t COLOR_ACCENT2 = 0x00C853;
const uint32_t COLOR_SELECT = 0xCCFF90;
const uint32_t COLOR_LINE = 0x00FF66;

const uint8_t MAX_RECORDS = 24;
const uint16_t MAX_BODY_CHARS = 260;
const uint8_t WRAP_COLS = 26;

struct Record {
  String id;
  String title;
  String body;
};

Record records[MAX_RECORDS];
uint8_t recordCount = 0;
int currentIndex = 0;
String dbName = "TTDB";
bool sdOk = false;
bool ttdbOk = false;
uint32_t ttdbSize = 0;
String sdStatus = "SD: --";
String fileStatus = "";

unsigned long lastInputMs = 0;
unsigned long lastTiltMs = 0;
const unsigned long INPUT_DEBOUNCE_MS = 220;
const unsigned long TILT_DEBOUNCE_MS = 260;

void setup() {
  k10.begin();
  playStartupToot();
  k10.initScreen(SCREEN_DIR);
  k10.creatCanvas();
  
  k10.canvas->canvasClear(COLOR_BG);
  k10.canvas->canvasCircle(120, 120, 30, COLOR_LINE, COLOR_LINE, true);
  k10.canvas->canvasText("TTDB Boot", 2, COLOR_TEXT);

  k10.canvas->updateCanvas();
  render();

  delay(250);
  
  k10.initSDFile();

  sdOk = SD.begin();
  sdStatus = sdOk ? "SD: OK" : "SD: FAIL";
  
  loadTTDB();
  
}

void loop() {

  handleButtons();
  handleTilt();
  delay(10);
  k10.canvas->updateCanvas();
  render();
}

void playStartupToot() {
  delay(50);
  music.playTone(196, 2000);
  music.playTone(262, 4000);
}

void handleButtons() {
  unsigned long now = millis();
  if (now - lastInputMs < INPUT_DEBOUNCE_MS) {
    return;
  }

  if (k10.buttonA->isPressed()) {
    selectPrev();
    lastInputMs = now;
    render();
    return;
  }

  if (k10.buttonB->isPressed()) {
    selectNext();
    lastInputMs = now;
    render();
  }
}

void handleTilt() {
  unsigned long now = millis();
  if (now - lastTiltMs < TILT_DEBOUNCE_MS) {
    return;
  }

  if (k10.isGesture(TiltLeft)) {
    selectPrev();
  } else if (k10.isGesture(TiltRight)) {
    selectNext();
  } else {
    return;
  }

  lastTiltMs = now;
  render();
}

void selectPrev() {
  if (recordCount == 0) {
    return;
  }
  currentIndex = (currentIndex - 1 + recordCount) % recordCount;
}

void selectNext() {
  if (recordCount == 0) {
    return;
  }
  currentIndex = (currentIndex + 1) % recordCount;
}

void loadTTDB() {
  recordCount = 0;
  dbName = "ttdb_dice_k10.md";
  ttdbOk = false;
  ttdbSize = 0;
  sdStatus = sdOk ? "SD: OK" : "SD: FAIL";
  fileStatus = "";

  if (!sdOk) {
    dbName = "SD init failed";
    addFallbackRecord();
    return;
  }

  File file = SD.open(TTDB_PATH);
  if (!file) {
    dbName = "TTDB (missing)";
    fileStatus = "File: MISSING";
    addFallbackRecord();
    return;
  }
  ttdbOk = true;
  ttdbSize = file.size();
  fileStatus = "File: OK " + String(ttdbSize) + "B";

  bool inMmpdb = false;
  int current = -1;
  while (file.available() && recordCount < MAX_RECORDS) {
    String line = file.readStringUntil('\n');
    line.trim();
    if (line.length() == 0) {
      continue;
    }

    if (line.startsWith("```mmpdb")) {
      inMmpdb = true;
      continue;
    }
    if (line.startsWith("```") && inMmpdb) {
      inMmpdb = false;
      continue;
    }
    if (inMmpdb && line.startsWith("db_name:")) {
      dbName = line.substring(String("db_name:").length());
      dbName.trim();
      dbName.replace("\"", "");
      dbName.replace("'", "");
      continue;
    }

    if (line.startsWith("---")) {
      continue;
    }

    if (line.startsWith("@LAT")) {
      current++;
      if (current >= MAX_RECORDS) {
        break;
      }
      records[current] = Record();
      records[current].id = extractId(line);
      records[current].title = records[current].id;
      records[current].body = "";
      recordCount = current + 1;
      continue;
    }

    if (current >= 0 && line.startsWith("## ")) {
      records[current].title = line.substring(3);
      continue;
    }

    if (current >= 0) {
      appendBody(records[current].body, line);
    }
  }

  if (recordCount == 0) {
    addFallbackRecord();
  }
}

String extractId(const String &line) {
  int pipeIndex = line.indexOf(" |");
  if (pipeIndex > 0) {
    return line.substring(0, pipeIndex);
  }
  return line;
}

void appendBody(String &body, const String &line) {
  if (body.length() >= MAX_BODY_CHARS) {
    return;
  }
  if (body.length() > 0) {
    body += " ";
  }
  String clean = line;
  clean.replace("**", "");
  clean.replace("*", "");
  body += clean;
  if (body.length() > MAX_BODY_CHARS) {
    body = body.substring(0, MAX_BODY_CHARS);
  }
}

void addFallbackRecord() {
  recordCount = 1;
  records[0].id = "@LAT0.0LON0.0";
  records[0].title = "No TTDB Found";
  records[0].body = "Copy ttdb_dice_k10.md to the SD root as /ttdb_dice_k10.md.";
}

void render() {
  k10.canvas->canvasClear(COLOR_BG);
  renderList();
  renderPreview();
  renderDiagnostics();
  k10.canvas->updateCanvas();
}

void renderList() {
  k10.canvas->canvasText(dbName, 7, COLOR_ACCENT);

  if (recordCount == 0) {
    k10.canvas->canvasText("No records found.", 9, COLOR_MUTED);
    return;
  }

  int start = max(0, currentIndex - 3);
  int end = min<int>(recordCount, start + 7);
  int row = 9;
  for (int i = start; i < end; i++) {
    String label = records[i].title;
    if (i == currentIndex) {
      k10.canvas->canvasText("> " + label, row, COLOR_SELECT);
    } else {
      k10.canvas->canvasText("  " + label, row, COLOR_TEXT);
    }
    row++;
  }
}

void renderPreview() {
  if (recordCount == 0) {
    return;
  }

  Record &rec = records[currentIndex];
  k10.canvas->canvasText(rec.id, 13, COLOR_MUTED);
  String preview = rec.body;
  if (preview.length() > 80) {
    preview = preview.substring(0, 80);
  }
  k10.canvas->canvasText(preview, 15, COLOR_TEXT);
  k10.canvas->canvasText("A/B: prev/next", 17, COLOR_MUTED);
}

void renderDiagnostics() {
  if (sdStatus.length() == 0) {
    sdStatus = "SD: --";
  }
  k10.canvas->canvasText(sdStatus, 2, sdOk ? COLOR_TEXT : COLOR_SELECT);
  if (sdOk) {
    k10.canvas->canvasText(fileStatus, 3, ttdbOk ? COLOR_TEXT : COLOR_SELECT);
  } else {
    k10.canvas->canvasText("File: --", 3, COLOR_MUTED);
  }
  String parsed = ttdbOk ? "Parsed: " + String(recordCount) : "Parsed: --";
  k10.canvas->canvasText(parsed, 4, COLOR_MUTED);
  k10.canvas->canvasText("Records: " + String(recordCount), 5, COLOR_MUTED);
}
