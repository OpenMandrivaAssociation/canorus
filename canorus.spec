%define beta rc3

Summary:	Music score editor
Name:		canorus
Version:	0.7.3
%if "%{beta}" != ""
Release:	0.%{beta}.1
%else
Release:	1
%endif
License:	GPLv2
Url:		https://canorus.sf.net/
Group:		Publishing
Source0:	https://vorboss.dl.sourceforge.net/project/canorus/%{version}/canorus-%{version}%{beta}.tar.bz2
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(alsa)
BuildRequires:	jackit-devel
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	portaudio-devel
BuildRequires:	lame-devel
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:    pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:    pkgconfig(Qt5WebEngineCore)
BuildRequires:    pkgconfig(Qt5WebEngineWidgets)
BuildRequires:    pkgconfig(Qt5QuickWidgets)
BuildRequires:    pkgconfig(Qt5Help)
BuildRequires:    pkgconfig(Qt5Designer)
BuildRequires:    pkgconfig(Qt5Test)
BuildRequires:    pkgconfig(Qt5UiTools)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	qt5-assistant
BuildRequires:	qt5-designer
BuildRequires:	qt5-devel >= 5.3
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-qtquick1

%description
Canorus is a free cross-platform music score editor. It supports an unlimited
number and length of staffs, polyphony, a MIDI playback of notes, chord
markings, lyrics, import/export filters to formats like MIDI, MusicXML,
ABC Music, MusiXTeX and LilyPond

%prep
%autosetup -p1 -n %{name}-%{version}%{beta}

%cmake_qt5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/canorus
%{_prefix}/lib/CanorusPython.py
%{_prefix}/lib/_CanorusPython.so
%{_prefix}/lib/__pycache__/CanorusPython.cpython-37.opt-1.pyc
%{_prefix}/lib/__pycache__/CanorusPython.cpython-37.pyc
%{_datadir}/%{name}
