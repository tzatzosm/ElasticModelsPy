#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 13/11/2017.
"""

from elasticmodelspy.index import Document
from elasticmodelspy.fields import KeywordField

class SimpleDocument(Document):
    first_name = KeywordField()
    sname = KeywordField(name='last_name')

def test_document_mapping():
    # Test mapping
    assert SimpleDocument.mapping() == {
        'first_name': {
            'type': 'keyword'
        },
        'last_name': {
            'type': 'keyword'
        }
    }

def test_document_instance_init():
    doc = SimpleDocument(**{
        'first_name': 'Marsel',
        'last_name': 'Tzatzo'
    })

    assert doc.first_name == 'Marsel'
    assert doc.sname == 'Tzatzo'


def test_document_instance_values():
    doc = SimpleDocument()
    doc.first_name = 'Marsel'
    doc.sname = 'Tzatzo'

    assert doc.first_name == 'Marsel'
    assert doc.sname == 'Tzatzo'

    assert doc.document() == {
        'first_name': 'Marsel',
        'last_name': 'Tzatzo'
    }

