import math

import pygame as pg


def distance(vec1, vec2):
    vec = [(vec2[i] - vec1[i]) for i in range(len(vec1))]
    return vector_length(vec)


def vector_length(vector_elem):
    add = 0
    for vec in vector_elem:
        add += vec ** 2
    return math.sqrt(add)


def normalize(pos):
    size = vector_length(pos)
    if size == 0:
        size = 1
    return [pos[0] / size, pos[1] / size]


def scalar(vec1, vec2):
    add = 0
    for i, j in zip(vec1, vec2):
        add += i * j
    return add


def determinant_2d(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def relative_position(vec1, vec2):
    return [(vec2[x] - vec1[x]) for x in range(2)]


class SegmentBuilder:
    def __init__(self, amount, segment_length, anchor_pos):
        self.amount = amount
        self.segment_length = segment_length
        self.anchor_pos = anchor_pos
        self.segments_parts = self.segment_builder()

    def segment_builder(self):
        segments = []
        for i in range(self.amount):
            segments.append(Segment([self.anchor_pos[0] + self.segment_length * i, self.anchor_pos[1]],
                                    0 + 10 * i, self.segment_length))
        return segments

    def draw_segments(self, screen, point):
        end = point
        for segment in reversed(self.segments_parts):
            segment.move(end)
            pg.draw.line(screen, (255, 255, 255), segment.pos, segment.pos_end, width=3)
            end = segment.pos


class Segment:
    def __init__(self, pos: list, angle: float, segment_length: int):
        self.pos = [pos[0], pos[1]]
        self.pos_end = [None, None]
        self.vector = [None, None]
        self.segment_length = segment_length
        self.angle = angle

    def follow(self, point):
        n_point = [(point[x] - self.pos[x]) for x in range(2)]
        norm_point = normalize(n_point)
        norm_vector = normalize([1, 0])

        dot = scalar(norm_vector, norm_point)
        det = determinant_2d(norm_vector, norm_point)
        angle = math.degrees(math.atan2(det, dot))
        self.angle = -angle

    def move(self, point):
        old_pos = self.pos
        self.pos = point
        self.follow(old_pos)
        self.pos = self.pos_end
        self.follow(point)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, n_angle):
        self._angle = math.radians(n_angle)
        self.pos_end = [math.cos(self._angle) * self.segment_length + self.pos[0],
                        -math.sin(self._angle) * self.segment_length + self.pos[1]]
        self.vector = relative_position(self.pos, self.pos_end)
