from concurrent.futures import ThreadPoolExecutor, as_completed


class Parallel:
    @staticmethod
    def run_parallel(fn, work_items, max_workers, fn_args=None):
        def get_args(item):
            args = [item]
            if fn_args and len(fn_args):
                args.extend(fn_args)
            return args

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(fn, *get_args(item)) for item in work_items]
            for future in as_completed(futures):
                results.append(future.result())
        return results

