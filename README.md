# SignBridge Server

Server/Backend for SignBridge App

* Use Docker for easy deployment.
* Needs `python3.8`, no other version works becuase it is dependent on `torch=1.1.0` which is used by `text2sign`
* more customizations or control on API is possible

# Docs

* Base URL

```
https://bipinkrish-signbridge.hf.space
```

### 1. Text to Gloss

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
{"gloss": "parliament see minute"}
```


### 2. Gloss to Sign

Takes a gloss text as input and returns fsw string which represents ham notation.

* Link

```
<base_url>/gloss2sign
```

* Params
  
```
gloss
```

* Example

```
https://bipinkrish-signbridge.hf.space/gloss2sign?gloss=today
```

```
{"sign": "M530x518S19a30500x482S19a38465x481S22f04509x506S22f14467x504"}
```

### 3. Sign to Image

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

```
{"img": img_base64}
```

![sign2img](https://github.com/SignBridgeApp/server/assets/87369440/b316d60e-921f-4205-a418-c13c08c66178)

### 4. Gloss to Pose

Takes a gloss text as input and returns combined pose vile visalized as image and words which are considerd.

* Link

```
<base_url>/gloss2pose
```

* Params
  
```
gloss
```

* Example

```
https://bipinkrish-signbridge.hf.space/gloss2pose?gloss=1 2 3
```

```
{"img": img_base64, "words": ["one", "two", "three"]}
```

![1 2 3](https://github.com/SignBridgeApp/server/assets/87369440/2066b7ea-b4b8-46d8-8ba7-dae9830b578d)
