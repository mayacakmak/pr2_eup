if (Meteor.isClient) {
  Template.body.helpers({
    interface_type: function() {
      return Session.get('interface_type');
    },
    interface_params: function() {
      return Session.get('interface_params');
    }
  });

  Template.body.onCreated(function() {
    var that = this;
    Session.setDefault('interface_type', 'default');
    Session.setDefault('interface_params', {});

    var ros = new ROSLIB.Ros({
      url : 'ws://localhost:9090'
    });
    ros.on('connection', function() {
      console.log('Connected to websocket server.');
    });
    ros.on('error', function(error) {
      console.log('Error connecting to websocket server: ', error);
    });
    ros.on('close', function() {
      console.log('Connection to websocket server closed.');
    });
    this.ros = ros;

    this.view_listener = new ROSLIB.Topic({
      ros: ros,
      name: 'rapid_robot/interface/interface_params',
      messageType: 'rapid_robot/InterfaceParams'
    });

    this.view_listener.subscribe(function(message) {
      Session.set('interface_type', message.interface_type);
      var params = {}
      for (var i=0; i<message.keys.length; i+=1) {
        var key = message.keys[i];
        var value = message.values[i];
        params[key] = value;
      }
      Session.set('interface_params', params);
    });

    this.view_publisher = new ROSLIB.Topic({
      ros: ros,
      name: 'rapid_robot/interface/interface_submissions',
      messageType: 'rapid_robot/InterfaceSubmissions'
    });
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
