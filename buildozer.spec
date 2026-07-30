[app]

# Название приложения
title = GameConfigGen

# Имя пакета
package.name = gameconfig

# Домен пакета
package.domain = org.test

# Директория с исходным кодом
source.dir = .

# Файлы, которые попадут в сборку
source.include_exts = py,png,jpg,kv,atlas,json

# Версия
version = 0.1

# Зависимости
requirements = python3,kivy==2.3.0

# Ориентация экрана
orientation = portrait

# Полноэкранный режим
fullscreen = 0

# --- Настройки Android ---

# Архитектуры (64-битные системы)
android.archs = arm64-v8a, armeabi-v7a

# Версии API и NDK
android.api = 34
android.minapi = 24
android.ndk = 25b

# Автоматическое принятие лицензий SDK
android.accept_sdk_license = True

[buildozer]

# Уровень логирования (2 - для подробных логов)
log_level = 2
warn_on_root = 1
