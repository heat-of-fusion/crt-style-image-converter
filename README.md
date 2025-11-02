# CRT-py
CRT-style image converter for python

<hr/>

![Demo Image](./src/results/pikachu.png)

<hr/>

## Requirement

- numpy
- opencv

<hr/>

## How to Use
Demo project is provided in ```demo.py```

```
import crtpy as crt

...

pattern = crt.PAT_HORIZONTAL_GLOW_6X6
converter = crt.CRTConverter(pattern)

crt, org = converter(image)
```

### How to use your own crt patterns
Just put your pattern path into ```crt.CRTCovnerter``` parameter.
```
...

your_pattern = f'./src/crt-patterns/YOUR_PATTERN.png'

converter = crt.CRTConverter(your_pattern)

...
```

<hr/>