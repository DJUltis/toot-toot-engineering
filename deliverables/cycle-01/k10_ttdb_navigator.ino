#include "unihiker_k10.h"
#include <SD.h>
#include <SPI.h>

UNIHIKER_K10 k10;

const uint8_t SCREEN_DIR = 2;
const char *TTDB_PATH = "/ttdb_dice_k10.md";

const uint32_t COLOR_BG = 0x000000;
const uint32_t COLOR_TEXT = 0x5C5C66;
const uint32_t COLOR_MUTED = 0x2F3238;
const uint32_t COLOR_ACCENT = 0x5A3D00;
const uint32_t COLOR_ACCENT2 = 0x4A2F00;
const uint32_t COLOR_SELECT = 0x3B4C66;

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
int scrollLine = 0;
bool detailView = false;
String dbName = "TTDB";

unsigned long lastInputMs = 0;
unsigned long lastTiltMs = 0;
const unsigned long INPUT_DEBOUNCE_MS = 220;
const unsigned long TILT_DEBOUNCE_MS = 260;

void setup() {
  k10.begin();
  k10.initScreen(SCREEN_DIR);
  k10.creatCanvas();
  k10.initSDFile();

  SD.begin();
  loadTTDB();
  render();
}

void loop() {
  handleButtons();
  handleTilt();
  delay(10);
}

void handleButtons() {
  unsigned long now = millis();
  if (now - lastInputMs < INPUT_DEBOUNCE_MS) {
    return;
  }

  if (k10.buttonAB->isPressed()) {
    detailView = !detailView;
    scrollLine = 0;
    lastInputMs = now;
    render();
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
  } else if (k10.isGesture(TiltForward)) {
    scrollDown();
  } else if (k10.isGesture(TiltBack)) {
    scrollUp();
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
  scrollLine = 0;
}

void selectNext() {
  if (recordCount == 0) {
    return;
  }
  currentIndex = (currentIndex + 1) % recordCount;
  scrollLine = 0;
}

void scrollUp() {
  if (!detailView) {
    return;
  }
  scrollLine = max(0, scrollLine - 1);
}

void scrollDown() {
  if (!detailView) {
    return;
  }
  int maxScroll = max(0, getBodyLineCount() - 12);
  scrollLine = min(maxScroll, scrollLine + 1);
}

void loadTTDB() {
  recordCount = 0;
  dbName = "TTDB";

  File file = SD.open(TTDB_PATH);
  if (!file) {
    dbName = "TTDB (missing)";
    addFallbackRecord();
    return;
  }

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
  if (detailView) {
    renderDetail();
  } else {
    renderList();
  }
  renderFooter();
  k10.canvas->updateCanvas();
}

void renderList() {
  k10.canvas->canvasText(dbName, 0, COLOR_ACCENT);

  if (recordCount == 0) {
    k10.canvas->canvasText("No records found.", 2, COLOR_MUTED);
    return;
  }

  int start = max(0, currentIndex - 5);
  int end = min<int>(recordCount, start + 10);
  int row = 2;
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

void renderDetail() {
  if (recordCount == 0) {
    k10.canvas->canvasText("No record selected.", 2, COLOR_MUTED);
    return;
  }

  Record &rec = records[currentIndex];
  k10.canvas->canvasText(rec.title, 0, COLOR_ACCENT2);
  k10.canvas->canvasText(rec.id, 1, COLOR_MUTED);

  String lines[40];
  int lineCount = wrapText(rec.body, lines, 40, WRAP_COLS);
  int row = 3;
  for (int i = scrollLine; i < lineCount && row < 16; i++) {
    k10.canvas->canvasText(lines[i], row, COLOR_TEXT);
    row++;
  }
}

void renderFooter() {
  String hint = detailView ? "A/B: prev/next  AB: list" : "A/B: prev/next  AB: detail";
  k10.canvas->canvasText(hint, 17, COLOR_MUTED);

  float ax = k10.getAccelerometerX();
  float ay = k10.getAccelerometerY();
  int cx = 185;
  int cy = 55;
  int r = 18;
  int dx = (int)(ax * 6);
  int dy = (int)(ay * 6);
  dx = max(-r + 4, min(r - 4, dx));
  dy = max(-r + 4, min(r - 4, dy));
  k10.canvas->canvasCircle(cx, cy, r, 0x141824, COLOR_MUTED, true);
  k10.canvas->canvasCircle(cx + dx, cy - dy, 4, COLOR_SELECT, COLOR_SELECT, true);
}

int wrapText(const String &text, String lines[], int maxLines, int maxCols) {
  int count = 0;
  String word = "";
  String line = "";
  for (int i = 0; i <= (int)text.length(); i++) {
    char c = i < (int)text.length() ? text[i] : ' ';
    if (c == ' ' || i == (int)text.length()) {
      if (word.length() == 0) {
        continue;
      }
      if (line.length() + word.length() + 1 > maxCols) {
        lines[count++] = line;
        line = word;
        if (count >= maxLines) {
          return count;
        }
      } else {
        if (line.length() > 0) {
          line += " ";
        }
        line += word;
      }
      word = "";
    } else {
      word += c;
    }
  }
  if (line.length() > 0 && count < maxLines) {
    lines[count++] = line;
  }
  return count;
}

int getBodyLineCount() {
  String lines[40];
  return wrapText(records[currentIndex].body, lines, 40, WRAP_COLS);
}
