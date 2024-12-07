from concurrent.futures import ThreadPoolExecutor, as_completed


class Parallel:
    @staticmethod
    def run_parallel(fn, work_items, max_workers, *fn_args):
        def get_args(item, *args):
            return [item, *args]

        if not work_items or not len(work_items):
            return []

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(fn, *get_args(item, *fn_args)) for item in work_items]
            for future in as_completed(futures):
                results.append(future.result())
        return results

