# Требования: указываем только python3 и kivy (Buildozer сам подтянет нужные версии)
requirements = python3,kivy==2.3.0

# Архитектуры: обязательно 64-битные системы для новых устройств
android.archs = arm64-v8a, armeabi-v7a

# Версии API и NDK
android.api = 34
android.minapi = 24
android.ndk = 25b

# Важно: разрешаем автоматическое скачивание Android SDK/NDK в облаке
android.accept_sdk_license = True
