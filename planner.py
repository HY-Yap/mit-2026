"""IPPT scoring and training-plan generation."""

AGE_BANDS = (
    {"label": "<22", "min": 0, "max": 21},
    {"label": "22-24", "min": 22, "max": 24},
    {"label": "25-27", "min": 25, "max": 27},
    {"label": "28-30", "min": 28, "max": 30},
    {"label": "31-33", "min": 31, "max": 33},
    {"label": "34-36", "min": 34, "max": 36},
    {"label": "37-39", "min": 37, "max": 39},
    {"label": "40-42", "min": 40, "max": 42},
    {"label": "43-45", "min": 43, "max": 45},
    {"label": "46-48", "min": 46, "max": 48},
    {"label": "49-51", "min": 49, "max": 51},
    {"label": "52-54", "min": 52, "max": 54},
    {"label": "55-57", "min": 55, "max": 57},
    {"label": "58-60", "min": 58, "max": 200},
)

AWARD_BANDS = (
    {"label": "Pass", "threshold": 51},
    {"label": "Pass with Incentive", "threshold": 61},
    {"label": "Silver", "threshold": 75},
    {"label": "Gold", "threshold": 85},
)

PUSHUP_ROWS = (
    (60, (25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (59, (24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (58, (24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (57, (24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (56, (24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (55, (23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (54, (23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25)),
    (53, (23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25)),
    (52, (23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25)),
    (51, (22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25, 25)),
    (50, (22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25)),
    (49, (22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25)),
    (48, (22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25)),
    (47, (21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25, 25)),
    (46, (21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25)),
    (45, (21, 21, 21, 22, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25)),
    (44, (21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 24, 24, 25, 25)),
    (43, (20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25, 25)),
    (42, (20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 24, 25, 25)),
    (41, (20, 20, 20, 21, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25)),
    (40, (20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 23, 23, 24, 25)),
    (39, (19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24)),
    (38, (19, 19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24)),
    (37, (19, 19, 19, 20, 20, 20, 20, 21, 21, 22, 22, 22, 23, 24)),
    (36, (18, 19, 19, 19, 20, 20, 20, 20, 21, 21, 22, 22, 23, 23)),
    (35, (18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 23)),
    (34, (18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 23)),
    (33, (17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 22, 22)),
    (32, (17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 22)),
    (31, (17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 22)),
    (30, (16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 21, 21)),
    (29, (16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 21)),
    (28, (16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20)),
    (27, (15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20)),
    (26, (15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19)),
    (25, (14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19)),
    (24, (13, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19)),
    (23, (12, 13, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18)),
    (22, (11, 12, 13, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18)),
    (21, (10, 11, 12, 13, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18)),
    (20, (9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 16, 17, 17, 17)),
    (19, (8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 16, 17, 17)),
    (18, (6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 16, 17)),
    (17, (4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 16)),
    (16, (2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16)),
    (15, (1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16)),
    (14, (0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15)),
    (13, (0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15)),
    (12, (0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14)),
    (11, (0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13)),
    (10, (0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12)),
    (9, (0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11)),
    (8, (0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10)),
    (7, (0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9)),
    (6, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8)),
    (5, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6)),
    (4, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4)),
    (3, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2)),
    (2, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)),
    (1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
)

SITUP_ROWS = (
    (60, (25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (59, (24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (58, (24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (57, (24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (56, (24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (55, (23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25)),
    (54, (23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25)),
    (53, (23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25)),
    (52, (23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25)),
    (51, (22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25, 25)),
    (50, (22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25)),
    (49, (22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25)),
    (48, (22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25)),
    (47, (21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25)),
    (46, (21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25)),
    (45, (21, 21, 21, 22, 22, 22, 22, 23, 23, 24, 24, 24, 25, 25)),
    (44, (21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 24, 24, 25, 25)),
    (43, (20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 25)),
    (42, (20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25)),
    (41, (20, 20, 20, 21, 21, 21, 21, 22, 22, 23, 23, 23, 24, 24)),
    (40, (20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 23, 23, 24, 24)),
    (39, (19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 24)),
    (38, (19, 19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 23)),
    (37, (18, 19, 19, 20, 20, 20, 20, 21, 21, 22, 22, 22, 23, 23)),
    (36, (18, 18, 19, 19, 20, 20, 20, 20, 21, 21, 22, 22, 22, 23)),
    (35, (17, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22)),
    (34, (16, 17, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22)),
    (33, (15, 16, 17, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22)),
    (32, (14, 15, 16, 17, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21)),
    (31, (14, 14, 15, 16, 17, 18, 18, 19, 19, 20, 20, 20, 21, 21)),
    (30, (13, 14, 14, 15, 16, 17, 18, 18, 19, 19, 20, 20, 20, 21)),
    (29, (13, 13, 14, 14, 15, 16, 17, 18, 18, 19, 19, 20, 20, 20)),
    (28, (12, 13, 13, 14, 14, 15, 16, 17, 18, 18, 19, 19, 20, 20)),
    (27, (11, 12, 13, 13, 14, 14, 15, 16, 17, 18, 18, 19, 19, 20)),
    (26, (10, 11, 12, 13, 13, 14, 14, 15, 16, 17, 18, 18, 19, 19)),
    (25, (9, 10, 11, 12, 13, 13, 14, 14, 15, 16, 17, 18, 18, 19)),
    (24, (8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 16, 17, 18, 18)),
    (23, (7, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 16, 17, 18)),
    (22, (7, 7, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 16, 17)),
    (21, (6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 16)),
    (20, (6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15)),
    (19, (5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 14, 14)),
    (18, (4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 14)),
    (17, (3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13)),
    (16, (2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13)),
    (15, (1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12)),
    (14, (0, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11)),
    (13, (0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10)),
    (12, (0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9)),
    (11, (0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8)),
    (10, (0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 7)),
    (9, (0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7)),
    (8, (0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6)),
    (7, (0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6)),
    (6, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5)),
    (5, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4)),
    (4, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3)),
    (3, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2)),
    (2, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)),
    (1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
)

RUN_ROWS = (
    ("8:30", (50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("8:40", (49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("8:50", (48, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:00", (47, 48, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:10", (46, 47, 48, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:20", (45, 46, 47, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:30", (44, 45, 46, 48, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:40", (43, 44, 45, 47, 48, 49, 50, 50, 50, 50, 50, 50, 50, 50)),
    ("9:50", (42, 43, 44, 46, 47, 48, 49, 50, 50, 50, 50, 50, 50, 50)),
    ("10:00", (41, 42, 43, 45, 46, 47, 48, 49, 50, 50, 50, 50, 50, 50)),
    ("10:10", (40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 50, 50, 50, 50)),
    ("10:20", (39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 50, 50, 50)),
    ("10:30", (38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 50)),
    ("10:40", (38, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50)),
    ("10:50", (37, 38, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)),
    ("11:00", (37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)),
    ("11:10", (36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48)),
    ("11:20", (36, 36, 37, 38, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47)),
    ("11:30", (35, 36, 36, 37, 38, 38, 39, 40, 41, 42, 43, 44, 45, 46)),
    ("11:40", (35, 35, 36, 37, 37, 38, 38, 39, 40, 41, 42, 43, 44, 45)),
    ("11:50", (34, 35, 35, 36, 37, 37, 38, 38, 39, 40, 41, 42, 43, 44)),
    ("12:00", (33, 34, 35, 36, 36, 37, 37, 38, 38, 39, 40, 41, 42, 43)),
    ("12:10", (32, 33, 34, 35, 36, 36, 37, 37, 38, 38, 39, 40, 41, 42)),
    ("12:20", (31, 32, 33, 35, 35, 36, 36, 37, 37, 38, 38, 39, 40, 41)),
    ("12:30", (30, 31, 32, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 40)),
    ("12:40", (29, 30, 31, 33, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39)),
    ("12:50", (28, 29, 30, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38, 38)),
    ("13:00", (27, 28, 29, 31, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38)),
    ("13:10", (26, 27, 28, 30, 31, 32, 33, 34, 35, 35, 36, 36, 37, 37)),
    ("13:20", (25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 35, 36, 36, 37)),
    ("13:30", (24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 35, 36, 36)),
    ("13:40", (23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 35, 36)),
    ("13:50", (22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 35)),
    ("14:00", (21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)),
    ("14:10", (20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34)),
    ("14:20", (19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)),
    ("14:30", (18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)),
    ("14:40", (16, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)),
    ("14:50", (14, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)),
    ("15:00", (12, 14, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)),
    ("15:10", (10, 12, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)),
    ("15:20", (8, 10, 12, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)),
    ("15:30", (6, 8, 10, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)),
    ("15:40", (4, 6, 8, 12, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25)),
    ("15:50", (2, 4, 6, 10, 12, 14, 16, 18, 19, 20, 21, 22, 23, 24)),
    ("16:00", (1, 2, 4, 8, 10, 12, 14, 16, 18, 19, 20, 21, 22, 23)),
    ("16:10", (0, 1, 2, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21, 22)),
    ("16:20", (0, 0, 1, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21)),
    ("16:30", (0, 0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20)),
    ("16:40", (0, 0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19)),
    ("16:50", (0, 0, 0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18)),
    ("17:00", (0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16)),
    ("17:10", (0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 10, 12, 14)),
    ("17:20", (0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 10, 12)),
    ("17:30", (0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 10)),
    ("17:40", (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8)),
    ("17:50", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6)),
    ("18:00", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4)),
    ("18:10", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2)),
    ("18:20", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)),
)


def parse_time_str(value):
    try:
        text = str(value).strip()
        if ":" in text:
            minutes, seconds = text.split(":", 1)
            return int(minutes) * 60 + int(round(float(seconds)))
        return int(round(float(text) * 60))
    except (TypeError, ValueError):
        return None


def time_to_seconds(minutes, seconds):
    return int(minutes) * 60 + int(seconds)


def seconds_to_time(total_seconds):
    total_seconds = max(0, int(round(total_seconds or 0)))
    return f"{total_seconds // 60}:{total_seconds % 60:02d}"


def age_group_index(age):
    try:
        value = int(age)
    except (TypeError, ValueError):
        value = 22
    for index, band in enumerate(AGE_BANDS):
        if band["min"] <= value <= band["max"]:
            return index
    return len(AGE_BANDS) - 1


def age_group(age):
    index = age_group_index(age)
    return {**AGE_BANDS[index], "index": index}


def _score_from_rows(value, rows, age):
    index = age_group_index(age)
    value = max(0, int(value or 0))
    if value >= rows[0][0]:
        return rows[0][1][index]
    for threshold, scores in rows:
        if value == threshold:
            return scores[index]
    return 0


def points_for_reps(reps, station="pushup", age=18):
    rows = SITUP_ROWS if station == "situp" else PUSHUP_ROWS
    return _score_from_rows(reps, rows, age)


def points_for_run(seconds, age=18):
    index = age_group_index(age)
    seconds = int(seconds or 0)
    for time_text, scores in RUN_ROWS:
        if seconds <= parse_time_str(time_text):
            return scores[index]
    return 0


def award_from_score(total, has_minimum_station_points=True):
    if not has_minimum_station_points:
        return "Fail"
    current = "Fail"
    for band in AWARD_BANDS:
        if total >= band["threshold"]:
            current = band["label"]
    return current


def calculate_ippt_score(pushups, situps, run_seconds, age=18):
    pushup_points = points_for_reps(pushups, "pushup", age)
    situp_points = points_for_reps(situps, "situp", age)
    run_points = points_for_run(run_seconds, age)
    total = pushup_points + situp_points + run_points
    has_minimum = min(pushup_points, situp_points, run_points) >= 1
    return {
        "total": total,
        "pushup_points": pushup_points,
        "situp_points": situp_points,
        "run_points": run_points,
        "grade": award_from_score(total, has_minimum),
        "has_minimum_station_points": has_minimum,
    }


def next_award_info(total):
    for band in AWARD_BANDS:
        if total < band["threshold"]:
            return {
                "next_grade": band["label"],
                "points_needed": band["threshold"] - total,
                "threshold": band["threshold"],
            }
    return {}


def reps_to_next_point(current_reps, station="pushup", age=18):
    current_reps = max(0, int(current_reps or 0))
    current_points = points_for_reps(current_reps, station, age)
    if current_points >= 25:
        return 0
    for reps in range(current_reps + 1, 61):
        if points_for_reps(reps, station, age) > current_points:
            return reps - current_reps
    return 0


def run_time_for_next_point(current_seconds, age=18):
    current_points = points_for_run(current_seconds, age)
    if current_points >= 50:
        return None
    return run_time_for_score(current_points + 1, age)


def run_time_for_score(required_points, age=18):
    if required_points <= 0:
        return parse_time_str(RUN_ROWS[-1][0])
    if required_points > 50:
        return None
    index = age_group_index(age)
    best_time = None
    for time_text, scores in RUN_ROWS:
        if scores[index] >= required_points:
            best_time = parse_time_str(time_text)
    return best_time


def generate_arithmetic_sequence(start, target, weeks):
    weeks = max(1, int(weeks or 1))
    if weeks == 1:
        return [int(round(target))]
    step = (target - start) / (weeks - 1)
    return [int(round(start + step * i)) for i in range(weeks)]


def generate_decreasing_geometric_sequence(start, target, weeks):
    weeks = max(1, int(weeks or 1))
    if weeks == 1:
        return [int(round(target))]
    if start <= 0 or target <= 0:
        return [int(round(target)) for _ in range(weeks)]
    if target >= start:
        return generate_arithmetic_sequence(start, target, weeks)
    ratio = (target / start) ** (1 / (weeks - 1))
    return [int(round(start * (ratio**i))) for i in range(weeks)]


def check_rep_progression(label, start, target, weeks):
    if weeks <= 1 or target <= start:
        return None
    weekly = (target - start) / (weeks - 1)
    if weekly > 8:
        return f"{label} target is unrealistic: about {weekly:.1f} extra reps per week."
    if weekly > 5:
        return f"{label} target is aggressive: about {weekly:.1f} extra reps per week."
    return None


def check_running_progression(start_seconds, target_seconds, weeks):
    if weeks <= 1 or target_seconds >= start_seconds:
        return None
    weekly = (start_seconds - target_seconds) / (weeks - 1)
    if weekly > 30:
        return f"Run target is unrealistic: about {weekly:.1f}s faster per week."
    if weekly > 15:
        return f"Run target is aggressive: about {weekly:.1f}s faster per week."
    return None


def get_scoring_data():
    return {
        "ageBands": AGE_BANDS,
        "awardBands": AWARD_BANDS,
        "pushupRows": PUSHUP_ROWS,
        "situpRows": SITUP_ROWS,
        "runRows": RUN_ROWS,
    }


def generate_training_plan(
    current_pushups,
    target_pushups,
    current_situps,
    target_situps,
    current_run_seconds,
    target_run_seconds,
    weeks,
    age=18,
):
    weeks = max(1, min(52, int(weeks or 1)))
    push_seq = generate_arithmetic_sequence(current_pushups, target_pushups, weeks)
    sit_seq = generate_arithmetic_sequence(current_situps, target_situps, weeks)
    run_seq = generate_decreasing_geometric_sequence(
        current_run_seconds, target_run_seconds, weeks
    )
    current_score = calculate_ippt_score(
        current_pushups, current_situps, current_run_seconds, age
    )
    target_score = calculate_ippt_score(
        target_pushups, target_situps, target_run_seconds, age
    )
    next_run_time = run_time_for_next_point(current_run_seconds, age)
    return {
        "age": age,
        "age_group": age_group(age),
        "push_seq": push_seq,
        "sit_seq": sit_seq,
        "run_seq": run_seq,
        "warnings": [
            warning
            for warning in (
                check_rep_progression("Push-up", current_pushups, target_pushups, weeks),
                check_rep_progression("Sit-up", current_situps, target_situps, weeks),
                check_running_progression(
                    current_run_seconds, target_run_seconds, weeks
                ),
            )
            if warning
        ],
        "current_score": current_score,
        "target_score": target_score,
        "next_point": {
            "pushup_reps": reps_to_next_point(current_pushups, "pushup", age),
            "situp_reps": reps_to_next_point(current_situps, "situp", age),
            "run_time": next_run_time,
            "run_time_display": seconds_to_time(next_run_time)
            if next_run_time is not None
            else None,
        },
        "suggestions": next_award_info(current_score["total"]),
        "target_suggestions": next_award_info(target_score["total"]),
    }
