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

class Personne(models.Model):
    class Meta:
        abstract = True

    GENRE_HOMME = 1
    GENRE_FEMME = 2
    GENRE_CHOICES = (
            (GENRE_HOMME, "homme"),
            (GENRE_FEMME, "femme"),
        )
    genre = models.PositiveSmallIntegerField(choices=GENRE_CHOICES)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(verbose_name="prénom", max_length=100)
    adresse = models.TextField()
    email = models.EmailField(blank=True, null=False)
    telephone = models.CharField(verbose_name="téléphone",
            max_length=20, blank=True, null=False)
    telephone_mobile = models.CharField(verbose_name="téléphone mobile",
            max_length=20, blank=True, null=False)
    adresse = models.TextField(blank=True, null=False)

class Candidat(Personne):
    num_psup = models.IntegerField(verbose_name="numéro Parcoursup",
            primary_key=True)
    date_naissance = models.DateField(verbose_name="date de naissance",
            blank=True, null=True)
    ine = models.CharField(blank=True, null=True,
            max_length=11, verbose_name="INE (numéro d'étudiant)",
            unique=True)

class ResponsableLegal(Personne):
    candidat = models.ForeignKey(Candidat, related_name='responsables',
            on_delete=models.CASCADE)
