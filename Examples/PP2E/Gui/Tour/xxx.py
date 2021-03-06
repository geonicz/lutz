##################################################################
# add tagged moves with time.sleep (not widget.after or threads);
# time.sleep does not block the gui event loop while pausing, but
# screen not redrawn until callback returns or widget.update call;
# the currently running onMove callback gets exclusive attention
# until it returns: others pause if press 'r' or 'o' during move;
##################################################################

from Tkinter import *
import canvasDraw, time

class CanvasEventsDemo(canvasDraw.CanvasEventsDemo):
    def __init__(self, parent=None):
        canvasDraw.CanvasEventsDemo.__init__(self, parent)
        self.canvas.create_text(75, 8, text='Press o and r to move shapes')
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)    
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)  
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged
    def create_oval_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_oval(x1, y1, x2, y2, fill='blue')
        self.canvas.addtag_withtag('ovals', objectId)
        return objectId
    def create_rectangle_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
        self.canvas.addtag_withtag('rectangles', objectId)
        return objectId
    def onMoveOvals(self, event):
        print 'moving ovals'
        self.moveInSquares(tag='ovals')           # move all tagged ovals
    def onMoveRectangles(self, event):
        print 'moving rectangles'
        self.moveInSquares(tag='rectangles')
    def printer(self):
        print 'hi'
        self.canvas.after(1000, self.printer)
    def moveInSquares(self, tag):                 # 5 reps of 4 times per sec
        self.canvas.after(1000, self.printer)
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                ##self.canvas.update()              # force screen redraw/update
                time.sleep(0.25)                  # pause, but don't block gui

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
