//$(document).ready(function(){
var following=[];
$.ajax({
  type: 'GET',
  url: 'https://api.twitch.tv/kraken/channels/twitch',
  headers: {
    'Client-ID': '1snou6w66xm4fy6ilucleh6gmbqd9j3'
  },
  success: function(data1) {
    if (data1.stream === null) {
      //FCC Offline
      $("#fccStatus").html("Free Code Camp is OFFLINE!");
    } else {
      //FCC Online
      $("#fccStatus").html("Free Code Camp is ONLINE!");
    }
  }

});

$.ajax({
  type: 'GET',
  url: 'https://api.twitch.tv/kraken/channels/twitch',
  headers: {
    'Client-ID': '1snou6w66xm4fy6ilucleh6gmbqd9j3'
  },
  success: function(data2) {
    for (var i = 0; i < data2.follows.length; i++) {
      var displayName = data2.follows[i].channel.display_name;
      following.push(displayName);
      var logo = data2.follows[i].channel.logo;
      var status = data2.follows[i].channel.status;
      if (logo == null) {
        logo = "https://static-cdn.jtvnw.net/jtv_user_pictures/twitch-channel_offline_image-d687d9e22677a1b6-1920x1080.png" // need to find logo
      }
      
      $("#followerInfo").prepend("<div class = 'row'>" + "<dic class='col-md-4'>" + "<img src='" + logo + "'>" + "</div>" + "<div class='col-md-4'>" + displayName + "</div>" + "<div class='col-md-4'>" + status + "</div></div>");

    }
 
  }
    
});


// dummy users freecode camp 
var deletedFollowers = ['brunofin', 'comster404'];
for (var i = 0; i < deletedFollowers.length; i++) {
  $.ajax({
    type: 'GET',
    url: 'https://api.twitch.tv/kraken/streams/' + deletedFollowers[i],
    headers: {
      'Client-ID': '1snou6w66xm4fy6ilucleh6gmbqd9j3'
    },
    error: function(data3) {
      var logo = "https://xxxx"; //need logo 
      var displayName = data3.statusText;
      var status = data3.status;
      $("#followerInfo").prepend("<div class = 'row'>" + "<dic class='col-md-4'>" + "<img src='" + logo + "'>" + "</div>" + "<div class='col-md-4'>" + displayname + "</div>" + "<div class='col-md-4'>" + status + "</div></div>");

    }
  });
}

//});