// aersia playlist js
const audio = document.querySelector('audio');

let g_playlist = null;
let g_previous = [];
let g_previous_idx = 0;
const MAX_HISTORY = 1;

const PLAYLISTS = {
	'VIP': 'https://vip.aersia.net/roster.xml',
	'Mellow': 'https://vip.aersia.net/roster-mellow.xml',
	'Source': 'https://vip.aersia.net/roster-source.xml',
	'Exiled': 'https://vip.aersia.net/roster-exiled.xml',
	'WAP': 'https://wap.aersia.net/roster.xml',
	'CPP': 'https://cpp.aersia.net/roster.xml',
};

const DEFAULT_PLAYLIST = 'VIP';

// Encodes location URI
function create_trackID(track) {
	let playlist = document.querySelector('#splaylist').value;
	let trackID = track.creator + ' - ' + track.title;
	trackID = trackID.replace(/[^a-zA-Z0-9-]/g, '_');

	return encodeURIComponent(playlist) + ':' + trackID;
}

// Decodes location URI
function parse_trackID(trackID) {
	let pieces = trackID.split(':');
	let playlist = null;
	let track = null;

	if(pieces.length < 2) {
		playlist = decodeURIComponent(trackID);
		track = '';
	} else {
		pieces.pop();
		playlist = decodeURIComponent(pieces.join(':'));
		track = trackID;
	}

	if(!(playlist in PLAYLISTS))
		return null;

	return {
		playlist: playlist,
		track: track
	};
}

function parse_XML(data) {
	result = [];
	
	playlist = data.getElementsByTagName('track');
	
	for (var i = 0; i < playlist.length; ++i) {
		track = {
			creator: playlist[i].getElementsByTagName('creator')[0].firstChild.nodeValue,
			title: playlist[i].getElementsByTagName('title')[0].firstChild.nodeValue,
			location: playlist[i].getElementsByTagName('location')[0].firstChild.nodeValue
		}
		result.push(track);
	}

	return result;
}

function load_XML(playlistURL, callback) {
	var xhttp = new XMLHttpRequest();
	xhttp.open("GET", playlistURL, true);
	xhttp.responseType = "document";
	xhttp.onreadystatechange = function () {
		if(this.readyState == xhttp.DONE && this.status == 200) {
			if(typeof callback === 'function')
				callback(xhttp.response);
		}
	}
	xhttp.onerror = function() {
		console.log("Error while getting XML.");
	}
	xhttp.send();
}

// clean-up below:

function play_next() {
	if (g_playlist === null)
		return;

	if (g_previous_idx >= (g_previous.length - 1)) {
		g_previous.push (Math.floor (Math.random () * g_playlist.length));
		g_previous_idx = g_previous.length - 1;
	}
	else {
		g_previous_idx += 1;
	}

	while (g_previous.length > MAX_HISTORY) {
		g_previous.shift ();
		g_previous_idx -= 1;
	}

	localStorage['volume'] = audio.volume;

	play_track (g_previous[g_previous_idx]);
}

function play_track(trackID) {
	var track = g_playlist[trackID];

	if (document.querySelector('.selected'))
		document.querySelector('.selected').classList.remove('selected');

	var trackelem = document.querySelectorAll(".playlist > div")[trackID];
	trackelem.classList.add('selected');

	window.location.hash = create_trackID(track);
	audio.setAttribute('src', track.location);
	audio.play();

	trackelem.scrollIntoView({behavior: "smooth", block: "center"});
}

function load_playlist(playlist, track) {
	var playlistURL = PLAYLISTS[playlist];
	var selected_track = track;

	localStorage['playlist'] = playlist;
	document.querySelector('#splaylist').value = playlist;

	// Clear
	document.querySelectorAll(".playlist > div").forEach(e => e.parentNode.removeChild(e));

	g_previous = [];
	g_previous_idx = 0;
	g_playlist = null;


	load_XML(playlistURL, function(data) {
		// Parse track list
		g_playlist = parse_XML(data);

		// Build HTML table for track listing
		for (var i = 0; i < g_playlist.length; ++i) {
			var track = g_playlist[i];

			// create a new div element 
			var row = document.createElement('div'); 
			// and give it some content 
			var newContent = document.createTextNode(track.creator + ' - ' + track.title); 
			// add the text node to the newly created div
			row.appendChild(newContent);  

			// add the newly created element and its content into the DOM 
			var currentDiv = document.querySelector('.playlist'); 
			currentDiv.appendChild(row);

			row.setAttribute('id', create_trackID(track));

			(function (i) {
				row.addEventListener('click', function (){
					play_track(i);
				}); 
			}) (i);
		}

		// Select specified track if possible, or play random track if not.
		var playlist_tracks = document.querySelectorAll(".playlist > div");
		let selection = 0;

		for (var i = 0; i < playlist_tracks.length; ++i) {
			if (playlist_tracks[i].id == selected_track){
				selection = playlist_tracks[i];
			}
		}

		if (selection != 0) {
			selection.click();
		} else {
			play_next();
		}

	});

};

function populatePlaylistOptions () {
	for (var name in PLAYLISTS) {
		var option = document.createElement('option'); 
		option.value = name;
		option.textContent = name;

		document.querySelector('#splaylist').appendChild(option);
	}
}

window.onload = function() {
	audio.addEventListener('error', function (){
		play_next();
	});

	audio.addEventListener('ended', function (){
		play_next();
	});

	document.querySelector('.next').addEventListener('click', function (){
		play_next(true);
	}); 

	document.querySelector('#splaylist').addEventListener('change', function (){
		var playlist = document.querySelector('#splaylist').value;
		load_playlist (playlist, '');
	}); 

	populatePlaylistOptions ();

	// Default playlist, random track
	var playlist = DEFAULT_PLAYLIST;
	var track = '';

	/* Load settings */
	if (localStorage.getItem ('volume') !== null)
		audio.volume = localStorage.getItem('volume');

	if (localStorage.getItem ('playlist') !== null) {
		if (localStorage.getItem ('playlist') in PLAYLISTS)
			playlist = localStorage.getItem ('playlist');
	}

	// If hash is set, override playlist and track
	var url_track = parse_trackID (window.location.hash.substring(1));

	if (url_track !== null) {
		playlist = url_track.playlist;
		track = url_track.track;
	}

	// Load playlist and track
	load_playlist (playlist, track);
};