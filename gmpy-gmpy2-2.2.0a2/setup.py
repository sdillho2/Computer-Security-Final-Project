import platform
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import shutil
from pathlib import Path

ON_WINDOWS = platform.system() == 'Windows'
_comp_args = ["DSHARED=1"]
sources = ['src/gmpy2.c']
winlibs = ['gmp.h','mpfr.h','mpc.h',
           'gmp.lib','mpfr.lib','mpc.lib',
           'libgmp-10.dll','libmpfr-6.dll','libmpc-3.dll',
           'libgcc_s_seh-1.dll','libwinpthread-1.dll']

# Copy the pre-built Windows libraries to the 'gmpy2' directory'.
# If you're not on Windows, delete the Windows libraries from the 'gmpy2'
# directory if the they exist.
src = Path('mingw64') / 'winlibs'
dst = Path('gmpy2')
if ON_WINDOWS:
    for filename in winlibs:
        try:
            shutil.copy(src / filename, dst / filename)
        except(FileNotFoundError):
            pass
else:
    for filename in winlibs:
        try:
            (dst / filename).unlink()
        except(FileNotFoundError):
            pass

class Gmpy2Build(build_ext):
    description = "Build gmpy2 with custom build options"
    user_options = build_ext.user_options + [
        ('fast', None,
         "Depend on MPFR and MPC internal implementations details"
         "(even more than the standard build)"),
        ('gcov', None, "Enable GCC code coverage collection"),
        ('vector', None, "Include the vector_XXX() functions;"
         "they are unstable and under active development"),
        ('static', None, "Enable static linking compile time options."),
        ('static-dir=', None, "Enable static linking and specify location."),
        ('gdb', None, "Build with debug symbols."),
    ]

    def initialize_options(self):
        build_ext.initialize_options(self)
        self.fast = False
        self.gcov = False
        self.vector = False
        self.static = False
        self.static_dir = False
        self.gdb = False

    def finalize_options(self):
        build_ext.finalize_options(self)
        self.force = 1
        if self.fast:
            _comp_args.append('DFAST=1')
        if self.gcov:
            if ON_WINDOWS:
                raise ValueError("Cannot enable GCC code coverage on Windows")
            _comp_args.append('DGCOV=1')
            _comp_args.append('O0')
            _comp_args.append('-coverage')
            self.libraries.append('gcov')
        if self.vector:
            _comp_args.append('DVECTOR=1')
        if self.static:
            _comp_args.remove('DSHARED=1')
            _comp_args.append('DSTATIC=1')
        if self.gdb:
            _comp_args.append('ggdb')
        if self.static_dir:
            _comp_args.remove('DSHARED=1')
            _comp_args.append('DSTATIC=1')
            self.include_dirs.append(self.static_dir + '/include')
            self.library_dirs.append(self.static_dir + '/lib')

    def build_extensions(self):
        compiler = self.compiler.compiler_type
        _prefix = '-' if compiler != 'msvc' else '/'
        for i in range(len(_comp_args)):
            _comp_args[i] = ''.join([_prefix, _comp_args[i]])
        build_ext.build_extensions(self)

extensions = [
    Extension('gmpy2.gmpy2',
              sources=sources,
              include_dirs=['./src'] + (['./gmpy2'] if ON_WINDOWS else []),
              libraries=['mpc','mpfr','gmp'] if ON_WINDOWS else ['mpc','mpfr','gmp','m'],
              library_dirs=(['./gmpy2'] if ON_WINDOWS else []),
              extra_compile_args=_comp_args,
              )
]

cmdclass = {'build_ext': Gmpy2Build}

setup(
    cmdclass=cmdclass,
    ext_modules=extensions,
)