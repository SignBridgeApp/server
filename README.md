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
```

* Example

```
https://bipinkrish-signbridge.hf.space/sign2img?sign=M530x518S19a30500x482S19a38465x481S22f04509x506S22f14467x504
```

![sign2img](https://github.com/SignBridgeApp/server/assets/87369440/c4cb6a05-fc47-4a6b-b324-91e0c2327451)
