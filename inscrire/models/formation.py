# -*- coding:utf8 -*-

# pyKol - Gestion de colles en CPGE
# Copyright (c) 2018 Florian Hatat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.db import models

class Etablissement(models.Model):
    """
    Établissement scolaire
    """
    pass

class Formation(models.Model):
    """
    Description d'une formation dispensée dans l'établissement
    """
    nom = models.CharField(max_length=100)
    code_parcoursup = models.SmallIntegerField(unique=True)
    groupe_parcoursup = models.SmallIntegerField()
    etablissement = models.ForeignKey(Etablissement,
            on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
