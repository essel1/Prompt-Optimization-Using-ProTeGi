import fire
import sys
import os

HUMAN_EVAL = "c:\Users\Sulav\Documents\UNI\7th semester\Deep Learning and Neural Network\Mini Project\Main\ProTeGi\HumanEval\data\HumanEval.jsonl.gz"
from human_eval.evaluation import evaluate_functional_correctness
# HUMAN_EVAL = "./human-eval-v2-20210705.jsonl"

print("Current Working Directory:", os.getcwd())


def entry_point(
    sample_file: str,
    k: str = "1,10,100",
    n_workers: int = 4,
    timeout: float = 3.0,
    problem_file: str = HUMAN_EVAL,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    k = list(map(int, k.split(",")))
    results = evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)
    print(results)


def main():
    fire.Fire(entry_point)


sys.exit(main())
