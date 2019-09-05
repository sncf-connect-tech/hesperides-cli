#!/usr/bin/env python
# coding: utf-8

from hesperidescli.local.descriptor_utils import substitute_all_mustaches
import pytest


def test_mustache_subst_with_extra_whitespaces():
    assert substitute_all_mustaches("{{ a | @default 42 }}", local_values={}) == "42"


def test_mustache_empty_pattern_ok():
    assert substitute_all_mustaches(r"{{b @pattern XXX}}", local_values={}) == ""


def test_mustache_empty_required_ko():
    with pytest.raises(ValueError) as subst_error:
        substitute_all_mustaches(r"{{c @required}}", local_values={})
    assert "Aucune valeur n'a été définie pour la moustache c" in str(subst_error.value)


def test_mustache_pattern_ok():
    template_content = r'{{marketLangs |@pattern "^\"([a-z]{2}|\*)-([A-Z]{2}|\*)\"(,\"([a-z]{2}|\*)-([A-Z]{2}|\*)\")*$" @default "\"fr-FR\",\"uk-EN\""}}'
    assert (
        substitute_all_mustaches(template_content, local_values={}) == '"fr-FR","uk-EN"'
    )


def test_mustache_pattern_digit_ok():
    template_content = r'{{hystrix_mur_threads | @default 40 @pattern "\\d+"}}'
    assert substitute_all_mustaches(template_content, local_values={}) == "40"


def test_mustache_pattern_fail():
    template_content = r'{{marketLangs |  @pattern   "^\"([a-z]{2}|\*)-([A-Z]{2}|\*)\"(,\"([a-z]{2}|\*)-([A-Z]{2}|\*)\")*$" }}'
    with pytest.raises(ValueError) as subst_error:
        substitute_all_mustaches(template_content, local_values={"marketLangs": "XXX"})
    assert "La valeur XXX ne respecte pas le @pattern" in str(subst_error.value)


def test_mustache_subst_empty_iterable():
    template_content = """[
  {{#products.configuration}}
  {
    "productType": "{{productType}}"
  },
  {{/products.configuration}}
  {}
]"""
    local_values = {"products.configuration": []}
    assert substitute_all_mustaches(template_content, local_values) == "[\n  {}\n]"


def test_mustache_subst_iterable():
    template_content = """[
  {{#products.configuration}}
  {
    "productType": "{{productType |@pattern "^[A-Z]*$" @required @comment "Type du produit. Ex : HOTEL" }}",
    "marketLangs": [
      {{marketLangs |@pattern "^\"([a-z]{2}|\\*)\\-([A-Z]{2}|\\*)\"(\\,\"([a-z]{2}|\\*)\\-([A-Z]{2}|\\*)\")*$" @comment "Couple marché-langue cible. ex : \"fr-FR\",\"uk-EN\""}}
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": {{daysFromToday |@default null @comment "Nombre (en jours) pour calculer la date minimale du voyage aller. Peut être négatif ou positif."}},
      "minStayLengthInDays": {{minStayLengthInDays |@default null @comment "Nombre de nuitées minimales du séjour"}},
      "maxStayLengthInDays": {{maxStayLengthInDays |@default null @comment "Nombre de nuitées maximales du séjour"}}
    },
    "murServiceName": {{murServiceName |@default null @comment "Propriété JSON de configuration d'éligibilité de service par destination"}}
  },
  {{/products.configuration}}
  {}
]"""
    local_values = {
        "products.configuration": [
            {
                "productType": "HOTEL",
                "marketLangs": '"fr-FR"',
                "daysFromToday": 0,
                "minStayLengthInDays": 1,
                "maxStayLengthInDays": 27,
                "murServiceName": None,
            },
            {
                "productType": "IDAVIS",
                "marketLangs": '"*-*"',
                "daysFromToday": 0,
                "minStayLengthInDays": None,
                "maxStayLengthInDays": None,
                "murServiceName": '"Avis"',
            },
            {
                "productType": "ARTICLE",
                "marketLangs": '"*-FR"',
                "daysFromToday": None,
                "minStayLengthInDays": None,
                "maxStayLengthInDays": None,
                "murServiceName": None,
            },
            {
                "productType": "VOITURE",
                "marketLangs": '"fr-FR"',
                "daysFromToday": 0,
                "minStayLengthInDays": None,
                "maxStayLengthInDays": None,
                "murServiceName": '"Avis"',
            },
            {
                "productType": "IDCAB",
                "marketLangs": '"*-FR"',
                "daysFromToday": None,
                "minStayLengthInDays": None,
                "maxStayLengthInDays": None,
                "murServiceName": '"iDCAB"',
            },
            {
                "productType": "OUICAR",
                "marketLangs": '"*-FR"',
                "daysFromToday": None,
                "minStayLengthInDays": None,
                "maxStayLengthInDays": None,
                "murServiceName": '"OUICARService"',
            },
        ]
    }
    expected_result = """[
  {
    "productType": "HOTEL",
    "marketLangs": [
      "fr-FR"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": 0,
      "minStayLengthInDays": 1,
      "maxStayLengthInDays": 27
    },
    "murServiceName": null
  },
  {
    "productType": "IDAVIS",
    "marketLangs": [
      "*-*"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": 0,
      "minStayLengthInDays": null,
      "maxStayLengthInDays": null
    },
    "murServiceName": "Avis"
  },
  {
    "productType": "ARTICLE",
    "marketLangs": [
      "*-FR"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": null,
      "minStayLengthInDays": null,
      "maxStayLengthInDays": null
    },
    "murServiceName": null
  },
  {
    "productType": "VOITURE",
    "marketLangs": [
      "fr-FR"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": 0,
      "minStayLengthInDays": null,
      "maxStayLengthInDays": null
    },
    "murServiceName": "Avis"
  },
  {
    "productType": "IDCAB",
    "marketLangs": [
      "*-FR"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": null,
      "minStayLengthInDays": null,
      "maxStayLengthInDays": null
    },
    "murServiceName": "iDCAB"
  },
  {
    "productType": "OUICAR",
    "marketLangs": [
      "*-FR"
    ],
    "tripDatesEligibilityConfiguration": {
      "daysFromToday": null,
      "minStayLengthInDays": null,
      "maxStayLengthInDays": null
    },
    "murServiceName": "OUICARService"
  },
  {}
]"""
    assert substitute_all_mustaches(template_content, local_values) == expected_result
