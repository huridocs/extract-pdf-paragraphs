from huggingface_hub import hf_hub_download

import config

paragraph_extraction_model_path = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="paragraph_extraction_model.model",
    revision="f80a08c4efec5e4c61624c78e5d733d9261b9c86",
    cache_dir=config.HUGGINGFACE_PATH,
)

letter_corpus_path = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="letter_corpus.txt",
    revision="da00a69c8d6a84493712e819580c0148757f466c",
    cache_dir=config.HUGGINGFACE_PATH,
)

toc_model_path = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="TwoModelsV3SegmentsContext2Len.model",
    revision="d66b49062439d6283464edadd9428a186c553f64",
    cache_dir=config.HUGGINGFACE_PATH,
)
