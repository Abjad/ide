# -*- encoding: utf-8 -*-
import os
from abjad import *
import ide
configuration = ide.tools.idetools.Configuration()


def test_Configuration__path_to_storehouse_01():
    
    storehouse = os.path.join(
        configuration.scores_directory,
        'foo_score',
        'foo_score',
        'stylesheets',
        )

    assert configuration._path_to_storehouse(storehouse) == storehouse

    path_1 = os.path.join(storehouse, 'foo')
    assert configuration._path_to_storehouse(path_1) == storehouse
        
    path_2 = os.path.join(storehouse, 'foo', 'bar')
    assert configuration._path_to_storehouse(path_1) == storehouse


def test_Configuration__path_to_storehouse_02():
    
    storehouse = os.path.join(
        configuration.example_scores_directory,
        'red_example_score',
        'red_example_score',
        'stylesheets',
        )

    assert configuration._path_to_storehouse(storehouse) == storehouse

    path_1 = os.path.join(storehouse, 'foo')
    assert configuration._path_to_storehouse(path_1) == storehouse
        
    path_2 = os.path.join(storehouse, 'foo', 'bar')
    assert configuration._path_to_storehouse(path_1) == storehouse