Name:		alacenc
Version:	0.4.1
Release:	2
Summary:	Encode audio into the Apple Lossless Audio Codec (ALAC) format
URL:		https://github.com/flacon/alacenc
License:	GPL
Group:		Sound/Utilities
Source0:	https://github.com/flacon/alacenc/archive/v%{version}/%{name}-%{version}.tar.gz
# See for patch - https://github.com/flacon/alacenc/issues/1
Patch0:     https://github.com/flacon/alacenc/commit/7e8d065b7dd405f4be0841fed6887079992029d4.patch

BuildSystem:	cmake
BuildRequires:	cmake
BuildRequires:	ninja

%description
alacenc - encode audio into the Apple Lossless Audio Codec (ALAC) format.

%prep
%autosetup -p1

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE