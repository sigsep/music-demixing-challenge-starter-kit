from test import CopyPredictor, ScaledMixturePredictor
from test_umx import UMXPredictor
from test_xumx import XUMXPredictor

# Predictor which does nothing
copy_predictor = CopyPredictor()

# Predictor which uses 1/4*mixture as separations
scaledmixture_predictor = ScaledMixturePredictor()

# UMX needs `models` folder to be present in your submission, check test_umx.py to learn more
# umx_predictor = UMXPredictor()

# X-UMX needs `models` folder to be present in your submission, check test_xumx.py to learn more
# xumx_predictor = XUMXPredictor()

"""
PARTICIPANT_TODO: The implementation you want to submit as your submission
"""
submission = scaledmixture_predictor
submission.run()
print("Successfully completed music demixing...")
