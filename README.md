# 2D optimal transport

## Install

    uv sync
    uv run points.py > dataset.txt  # Generate points
    make mcmf  # Or g++-15 mcmf.cpp -o mcmf but you need g++ not stupid Mac clang
    ./mcmf < dataset.txt > matching.txt
    uv run plot.py

## Examples

![](matching.png)

![](matching2.png)
