Name:		alacenc
Version:	0.4.2
Release:	1
Summary:	Encode audio into the Apple Lossless Audio Codec (ALAC) format
License:	MIT
Group:		Sound/Utilities
URL:		https://github.com/flacon/alacenc
Source0:	https://github.com/flacon/alacenc/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	cmake
BuildOption:	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
BuildOption:	-DCMAKE_C_FLAGS="%{optflags}"
BuildOption:	-DCMAKE_CXX_FLAGS="%{optflags}"
BuildOption:	-DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption:	-GNinja

BuildRequires:	cmake
BuildRequires:	ninja

%description
alacenc - encode audio into the Apple Lossless Audio Codec (ALAC) format.

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE
