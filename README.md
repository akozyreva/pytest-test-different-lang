# Pytest-test-different-lang
It's an example of how can be parametrized language.

## Structure
conftest.py - add lang option. Add browser fixture, which accpets this option.
test_items.py - test, which opens page, verifies button and prints the text of button.

## How to run
In root dir:

```pytest -s --language=es```