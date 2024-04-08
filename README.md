# SignBridge Server

Server/Backend for SignBridge App

# Docs

* Base URL

```
https://bipinkrish-signbridge.hf.space
```

### 1. Text to Sign

Takes a spoken text as input and returns fsw string which represents ham notation.

* Link

```
<base_url>/text2sign
```

* Params
  
```
text
```

* Example

```
https://bipinkrish-signbridge.hf.space/text2sign?text=today
```

```
{"sign": "M530x518S19a30500x482S19a38465x481S22f04509x506S22f14467x504"}
```

### 2. Sign to Image

Takes a fsw string as input and returns image of ham notation.

* Link

```
<base_url>/sign2img
```

* Params
  
```
sign
line_color (Optional)
```

* Example

```
https://bipinkrish-signbridge.hf.space/sign2img?sign=M530x518S19a30500x482S19a38465x481S22f04509x506S22f14467x504&line_color=10,23,122,255
```

![sign2img](https://github.com/SignBridgeApp/server/assets/87369440/542e93ed-3138-47b2-a777-4aa0739b6cf7)

### 3. Text to Gloss

Takes a spoken english text as input and returns simplified gloss of it.

* Link

```
<base_url>/text2gloss
```

* Params
  
```
text
```

* Example

```
https://bipinkrish-signbridge.hf.space/text2gloss?text=membership%20of%20parliament%20see%20minutes
```

```
{"gloss":"parliament see minute"}
```
