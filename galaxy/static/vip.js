var g_playlist=null,g_previous=[],g_previous_idx=0,MAX_HISTORY=3,PLAYLISTS={VIP:"https://vip.aersia.net/roster.xml",Mellow:"https://vip.aersia.net/roster-mellow.xml",Source:"https://vip.aersia.net/roster-source.xml",Exiled:"https://vip.aersia.net/roster-exiled.xml",WAP:"https://wap.aersia.net/roster.xml",CPP:"https://cpp.aersia.net/roster.xml"},DEFAULT_PLAYLIST="VIP";function createTrackId(t){var l=$("#splaylist").val();return t=(t=t.creator+" - "+t.title).replace(/[^a-zA-Z0-9-]/g,"_"),encodeURIComponent(l)+":"+t}function parseTrackId(t){var l=t.split(":"),e="",a="";return l.length<2?(e=decodeURIComponent(t),a=""):(l.pop(),e=decodeURIComponent(l.join(":")),a=t),e in PLAYLISTS?{playlist:e,track:a}:null}function parsePlaylist(t){return result=[],$(t).find("playlist trackList > track").each(function(){track={creator:$(this).find("creator").text(),title:$(this).find("title").text(),location:$(this).find("location").text()},result.push(track)}),result}function playPreviousTrack(){null!==g_playlist&&(g_previous_idx<=0?g_previous_idx=0:g_previous_idx-=1,playTrack(g_previous[g_previous_idx]))}function playNextTrack(){if(null!==g_playlist){for(g_previous_idx>=g_previous.length-1?(g_previous.push(Math.floor(Math.random()*g_playlist.length)),g_previous_idx=g_previous.length-1):g_previous_idx+=1;g_previous.length>MAX_HISTORY;)g_previous.shift(),g_previous_idx-=1;playTrack(g_previous[g_previous_idx])}}function playTrack(t){var l=g_playlist[t];$(".playlist .selected").removeClass("selected");var e=$(".playlist div").eq(t);e.addClass("selected"),window.location.hash=createTrackId(l),$("audio").attr("src",l.location),$("audio").trigger("play"),$("html, body").stop().animate({scrollTop:e.offset().top-$("header").height()},1e3)}function loadNewPlaylist(t,l){var e=PLAYLISTS[t],a=l;localStorage.playlist=t,$("#splaylist").val(t),$(".playlist div").remove(),g_previous=[],g_previous_idx=0,g_playlist=null,$.ajax({url:e,success:function(t){g_playlist=parsePlaylist(t);for(var l=0;l<g_playlist.length;++l){var e=g_playlist[l],i=$("<div>");i.text(e.creator+" - "+e.title),i.attr("id",createTrackId(e)),i.appendTo(".playlist"),function(t){i.click(function(){playTrack(t)})}(l)}var r=$(".playlist div").filter(function(t,l){return l.id==a});r.length>0?r[0].click():playNextTrack()}})}function populatePlaylistOptions(){for(var t in PLAYLISTS){var l=$("<option>");l.val(t),l.text(t),$("#splaylist").append(l)}}$(function(){$("audio").on("error",function(){playNextTrack()}),$("audio").on("ended",function(){playNextTrack()}),$(".next").click(function(){playNextTrack(!0)}),$(".previous").click(function(){playPreviousTrack()}),$("#splaylist").on("change",function(){loadNewPlaylist($("#splaylist").val(),"")}),populatePlaylistOptions();var t=DEFAULT_PLAYLIST,l="";null!==localStorage.getItem("volume")&&($("audio").get(0).volume=localStorage.getItem("volume")),null!==localStorage.getItem("playlist")&&localStorage.getItem("playlist")in PLAYLISTS&&(t=localStorage.getItem("playlist"));var e=parseTrackId(window.location.hash.substr(1));null!==e&&(t=e.playlist,l=e.track),loadNewPlaylist(t,l)});