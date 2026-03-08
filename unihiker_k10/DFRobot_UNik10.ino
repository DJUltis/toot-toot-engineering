#include "unihiker_k10.h"

UNIHIKER_K10 k10;

void setup() {
  k10.begin();

  // 2 is used in DFRobot's examples as a common screen direction setting.
  uint8_t screen_dir = 2;

  k10.initScreen(screen_dir);
  k10.creatCanvas();

  // (text, row, color). Rows are line numbers on the canvas.
  k10.canvas->canvasText("Hello, World!", 2, 0xFFFFFF);
  k10.canvas->canvasText("UNIHIKER K10",   4, 0x00FF00);

  k10.canvas->updateCanvas();
}

void loop() {
  // nothing
}
