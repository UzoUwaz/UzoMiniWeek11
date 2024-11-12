The operation is load data

The truncated output is:

|    |   ID | name    |   total |   male_share |   female_share |       gap |
|---:|-----:|:--------|--------:|-------------:|---------------:|----------:|
|  0 |    1 | Casey   |     nan |     0.584287 |       0.415713 | 0.168573  |
|  1 |    2 | Riley   |     nan |     0.507639 |       0.492361 | 0.0152781 |
|  2 |    3 | Jessie  |     nan |     0.477834 |       0.522166 | 0.0443315 |
|  3 |    4 | Jackie  |     nan |     0.421133 |       0.578867 | 0.157735  |
|  4 |    5 | Avery   |     nan |     0.335213 |       0.664787 | 0.329574  |
|  5 |    6 | Jaime   |     nan |     0.561793 |       0.438207 | 0.123586  |
|  6 |    7 | Peyton  |     nan |     0.433719 |       0.566281 | 0.132561  |
|  7 |    8 | Kerry   |     nan |     0.483949 |       0.516051 | 0.0321023 |
|  8 |    9 | Jody    |     nan |     0.352068 |       0.647932 | 0.295864  |
|  9 |   10 | Kendall |     nan |     0.372367 |       0.627633 | 0.255267  |

The operation is describe data

The truncated output is:

|    | summary   |      ID | name    |   total |   male_share |   female_share |           gap |
|---:|:----------|--------:|:--------|--------:|-------------:|---------------:|--------------:|
|  0 | count     | 919     | 919     |       0 |  919         |    919         | 919           |
|  1 | mean      | 460     |         |         |    0.507206  |      0.492794  |   0.173863    |
|  2 | stddev    | 265.437 |         |         |    0.0994233 |      0.0994233 |   0.0973997   |
|  3 | min       |   1     | Aalijah |         |    0.333561  |      0.333722  |   7.17281e-05 |
|  4 | max       | 919     | Zohar   |         |    0.666278  |      0.666439  |   0.332879    |

The operation is query data

The query is SELECT * FROM unisexdb WHERE total > 10000 AND male_share > 0.5;

The truncated output is:

| ID   | name   | total   | male_share   | female_share   | gap   |
|------|--------|---------|--------------|----------------|-------|

The operation is transform data

The truncated output is:

|    |   ID | name    |   total |   male_share |   female_share |       gap | Gender_Category   |
|---:|-----:|:--------|--------:|-------------:|---------------:|----------:|:------------------|
|  0 |    1 | Casey   |     nan |     0.584287 |       0.415713 | 0.168573  | Primarily Male    |
|  1 |    2 | Riley   |     nan |     0.507639 |       0.492361 | 0.0152781 | Primarily Male    |
|  2 |    3 | Jessie  |     nan |     0.477834 |       0.522166 | 0.0443315 | Primarily Female  |
|  3 |    4 | Jackie  |     nan |     0.421133 |       0.578867 | 0.157735  | Primarily Female  |
|  4 |    5 | Avery   |     nan |     0.335213 |       0.664787 | 0.329574  | Primarily Female  |
|  5 |    6 | Jaime   |     nan |     0.561793 |       0.438207 | 0.123586  | Primarily Male    |
|  6 |    7 | Peyton  |     nan |     0.433719 |       0.566281 | 0.132561  | Primarily Female  |
|  7 |    8 | Kerry   |     nan |     0.483949 |       0.516051 | 0.0321023 | Primarily Female  |
|  8 |    9 | Jody    |     nan |     0.352068 |       0.647932 | 0.295864  | Primarily Female  |
|  9 |   10 | Kendall |     nan |     0.372367 |       0.627633 | 0.255267  | Primarily Female  |

The operation is load data

The truncated output is:

|    |   ID | name    |   total |   male_share |   female_share |       gap |
|---:|-----:|:--------|--------:|-------------:|---------------:|----------:|
|  0 |    1 | Casey   |     nan |     0.584287 |       0.415713 | 0.168573  |
|  1 |    2 | Riley   |     nan |     0.507639 |       0.492361 | 0.0152781 |
|  2 |    3 | Jessie  |     nan |     0.477834 |       0.522166 | 0.0443315 |
|  3 |    4 | Jackie  |     nan |     0.421133 |       0.578867 | 0.157735  |
|  4 |    5 | Avery   |     nan |     0.335213 |       0.664787 | 0.329574  |
|  5 |    6 | Jaime   |     nan |     0.561793 |       0.438207 | 0.123586  |
|  6 |    7 | Peyton  |     nan |     0.433719 |       0.566281 | 0.132561  |
|  7 |    8 | Kerry   |     nan |     0.483949 |       0.516051 | 0.0321023 |
|  8 |    9 | Jody    |     nan |     0.352068 |       0.647932 | 0.295864  |
|  9 |   10 | Kendall |     nan |     0.372367 |       0.627633 | 0.255267  |

The operation is describe data

The truncated output is:

|    | summary   |      ID | name    |   total |   male_share |   female_share |           gap |
|---:|:----------|--------:|:--------|--------:|-------------:|---------------:|--------------:|
|  0 | count     | 919     | 919     |       0 |  919         |    919         | 919           |
|  1 | mean      | 460     |         |         |    0.507206  |      0.492794  |   0.173863    |
|  2 | stddev    | 265.437 |         |         |    0.0994233 |      0.0994233 |   0.0973997   |
|  3 | min       |   1     | Aalijah |         |    0.333561  |      0.333722  |   7.17281e-05 |
|  4 | max       | 919     | Zohar   |         |    0.666278  |      0.666439  |   0.332879    |

The operation is query data

The query is SELECT * FROM unisexdb WHERE total > 10000 AND male_share > 0.5;

The truncated output is:

| ID   | name   | total   | male_share   | female_share   | gap   |
|------|--------|---------|--------------|----------------|-------|

The operation is transform data

The truncated output is:

|    |   ID | name    |   total |   male_share |   female_share |       gap | Gender_Category   |
|---:|-----:|:--------|--------:|-------------:|---------------:|----------:|:------------------|
|  0 |    1 | Casey   |     nan |     0.584287 |       0.415713 | 0.168573  | Primarily Male    |
|  1 |    2 | Riley   |     nan |     0.507639 |       0.492361 | 0.0152781 | Primarily Male    |
|  2 |    3 | Jessie  |     nan |     0.477834 |       0.522166 | 0.0443315 | Primarily Female  |
|  3 |    4 | Jackie  |     nan |     0.421133 |       0.578867 | 0.157735  | Primarily Female  |
|  4 |    5 | Avery   |     nan |     0.335213 |       0.664787 | 0.329574  | Primarily Female  |
|  5 |    6 | Jaime   |     nan |     0.561793 |       0.438207 | 0.123586  | Primarily Male    |
|  6 |    7 | Peyton  |     nan |     0.433719 |       0.566281 | 0.132561  | Primarily Female  |
|  7 |    8 | Kerry   |     nan |     0.483949 |       0.516051 | 0.0321023 | Primarily Female  |
|  8 |    9 | Jody    |     nan |     0.352068 |       0.647932 | 0.295864  | Primarily Female  |
|  9 |   10 | Kendall |     nan |     0.372367 |       0.627633 | 0.255267  | Primarily Female  |

