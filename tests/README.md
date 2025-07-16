# Tests

AI prompt engineering and parameter testing for the language learning game.

## Files

### `test_temperature.py`
Tests temperature effects on word generation (0.1-1.0).

**Results**: Temperature 0.7-0.8 gives best variety for learning vocabulary.

## Run Tests

```bash
python tests/test_temperature.py
```

## Notes

- Temperature 0.1: Too predictable
- Temperature 0.7-0.8: Optimal for learning
- Temperature 1.0: Too random
