# pytl
### Python transactional language driver

#### Drivers

> > Adtran

> > AFC

> > Calix

#### Release scheme

Version identifiers are separated into up to five segments:

[N!]N(.N)*[{a|b|rc}N][.postN][.devN]

* Epoch segment: N!
* Release segment: N(.N)
* Pre-release segment: {a|b|rc}N
* Post-release segment: .postN
* Development release segment: .devN


X.YaN.devM       # Developmental release of an alpha release
X.YbN.devM       # Developmental release of a beta release
X.YrcN.devM      # Developmental release of a release candidate
X.Y.postN.devM   # Developmental release of a post-release
