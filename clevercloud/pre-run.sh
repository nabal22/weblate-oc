#!/usr/bin/env bash
set -euo pipefail

export DJANGO_SETTINGS_MODULE=settings
# Applique les migrations au démarrage (idempotent)
weblate migrate --noinput
# Collecte les fichiers statiques
weblate collectstatic --noinput
# Compile les traductions de Weblate lui-même
weblate compilemessages || true