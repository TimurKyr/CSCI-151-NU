languages = ['Python','Java','JavaScript','Go','Ruby','Dart','PHP','Scala','Kotlin','Rust','C++','C','Haskell']
leng, st = 0, ""
for s in languages:
    if len(s) > leng:
        leng = len(s)
        st = s