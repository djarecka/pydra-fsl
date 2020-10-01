import os, pytest
from pathlib import Path
from ..susan import SUSAN


@pytest.mark.parametrize(
    "inputs, outputs",
    [({"brightness_threshold": 0.01, "fwhm": 2}, ["out_file", "smoothed_file"])],
)
def test_SUSAN(inputs, outputs):
    in_file = Path(os.path.dirname(__file__)) / "data_tests/test.nii.gz"
    if inputs is None:
        inputs = {}
    for key, val in inputs.items():
        try:
            inputs[key] = eval(val)
        except:
            pass
    task = SUSAN(in_file=in_file, **inputs)
    assert set(task.generated_output_names) == set(
        ["return_code", "stdout", "stderr"] + outputs
    )


@pytest.mark.parametrize("inputs, error", [(None, "AttributeError")])
def test_SUSAN_exception(inputs, error):
    in_file = Path(os.path.dirname(__file__)) / "data_tests/test.nii.gz"
    if inputs is None:
        inputs = {}
    for key, val in inputs.items():
        try:
            inputs[key] = eval(val)
        except:
            pass
    task = SUSAN(in_file=in_file, **inputs)
    with pytest.raises(eval(error)):
        task.generated_output_names
