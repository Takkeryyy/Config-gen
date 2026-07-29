[app]
title = GameConfigGen
package.name = gameconfiggen
package.domain = org.config
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 1.0

# Строго базовые зависимости. Никаких ручных версий и лишних пакетов.
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True

# Проверенные стабильные параметры для сборки без багов
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
