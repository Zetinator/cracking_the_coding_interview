"""8.13 Stack of Boxes: You have a stack of n boxes, with widths Wi' heights hi' and depths d 1• The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height. and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
"""
class Box():
    def __init__(self, h: int, w: int, d: int):
        self.h = h
        self.w = w
        self.d = d
    def __repr__(self):
        return f'{(self.h, self.w, self.d)}'

def stack(boxes: list)-> int:
    """the classics...
    https://www.youtube.com/watch?v=krZI60lKPek&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=12
    """
    # sort boxes by one dimension
    boxes = sorted(boxes, key=lambda box: -box.h)
    def dp(boxes, state=(0,[])):
        if not boxes: return state
        # find compatible set
        compatible = []
        for box in boxes[1:]:
            if box.w < boxes[0].w and box.d < boxes[0].d:
                compatible.append(box)
        return max(dp(compatible, (state[0]+1, state[1]+[boxes[0]])),  # we take it
                   dp(boxes[1:], state),  # we dont...
                   key=lambda state: state[0])  # order by number of boxes in the stack
    return dp(boxes)

# test
from random import uniform
test = [Box(int(uniform(0,50)), int(uniform(0,50)), int(uniform(0,50))) for _ in range(5)]
print(f'test: {test}, biggest stack: {stack(test)}')
