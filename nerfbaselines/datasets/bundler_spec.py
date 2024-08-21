from ..registry import register


register({
    "id": "bundler",
    "load_dataset_function": ".bundler:load_bundler_dataset",
    "priority": 50,
})
