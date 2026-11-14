"""Run packing assertions against the real component in native Wasmtime."""
import subprocess
import unittest


def pack(request):
    return subprocess.check_output(
        ['wasmtime', 'run', '--invoke', f'pack({request})',
         'build.nosync/test/pack.wasm'], text=True).strip()


class PackingTests(unittest.TestCase):
    def test_packed_and_failed_rectangles(self):
        result = pack('{width: 8, height: 8, padding: 1, auto-size: false, '
                      'rects: [{id: none, width: 3, height: 2}, '
                      '{id: some(9), width: 2, height: 2}, '
                      '{id: none, width: 10, height: 1}]}')
        self.assertTrue(result.startswith('ok('), result)
        self.assertIn('packed-count: 2', result)
        self.assertIn('failed-count: 1', result)
        self.assertRegex(result, r'id: 9, x: some\(\d+\), y: some\(\d+\), width: 2, height: 2, packed: true')

    def test_invalid_dimensions(self):
        result = pack('{width: 0, height: 4, padding: 0, auto-size: false, rects: []}')
        self.assertTrue(result.startswith('err('), result)
        self.assertIn('code: invalid-arg', result)
