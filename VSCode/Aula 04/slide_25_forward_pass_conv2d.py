# AULA 04 — SLIDE 25 — Prática guiada: um forward pass com Conv2d
# O slide 26 interpreta os shapes impressos por este código.

import torch
import torch.nn as nn

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
conv = nn.Conv2d(
    in_channels=3,
    out_channels=8,
    kernel_size=3,
    padding=1
)

x = torch.randn(1, 3, 64, 64)
y = conv(x)

print(x.shape)
print(y.shape)
