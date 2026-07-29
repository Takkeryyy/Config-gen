[app]
title = GameConfigGen
package.name = gameconfiggen
package.domain = org.config
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 1.0

# Жестко только необходимые стабильные пакеты. Никакого мусора вроде "android" или точных версий.
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
- name: Set up Python 3.11
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'
