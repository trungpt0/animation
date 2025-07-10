import pygame
from animations.happy import draw_happy_face_offset, draw_happy_face_blink, screen

pygame.init()
clock = pygame.time.Clock()
DEL_SCREEN = (30, 30, 30)

# Các bước animation
steps = [
    {'start': (0, 0), 'end': (-140, -100), 'pause_after': 60, 'blink': False},
    {'start': (-140, -100), 'end': (0, 0), 'pause_after': 60, 'blink': True},
    {'start': (0, 0), 'end': (-140, 100), 'pause_after': 60, 'blink': False},
    {'start': (-140, 100), 'end': (0, 0), 'pause_after': 60, 'blink': True},
]

duration = 30  # số frame để trượt

# Trạng thái animation
current_step = 0
frame_in_step = 0
state = "moving"  # hoặc "pause"

running = True
while running:
    screen.fill(DEL_SCREEN)

    step = steps[current_step]
    start = step['start']
    end = step['end']
    pause_time = step['pause_after']

    if state == "moving":
        t = min(frame_in_step / duration, 1.0)
        x = int(start[0] + (end[0] - start[0]) * t)
        y = int(start[1] + (end[1] - start[1]) * t)
        draw_happy_face_offset(x, y)

        if frame_in_step >= duration:
            frame_in_step = 0
            state = "pause"
        else:
            frame_in_step += 1

    elif state == "pause":
        # Khung nháy mắt mượt (frame: height)
        blink_frames = {
            26: 400,
            27: 200,
            28: 100,
            29: 40,
            30: 100,
            31: 200,
            32: 400
        }

        if step['blink'] and frame_in_step in blink_frames:
            draw_happy_face_blink(end[0], end[1], blink_frames[frame_in_step])
        else:
            draw_happy_face_offset(end[0], end[1])

        if frame_in_step >= pause_time:
            current_step = (current_step + 1) % len(steps)
            frame_in_step = 0
            state = "moving"
        else:
            frame_in_step += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
