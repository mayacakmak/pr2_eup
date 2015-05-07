if (Meteor.isClient) {
  Template.body.helpers({
    interface_type: function() {
      return Template.instance().interface_type.get();
    },
    interface_params: function() {
      return Template.instance().interface_params.keys;
    }
  });

  Template.body.onCreated(function() {
    var that = this;
    this.interface_type = new ReactiveVar('default');
    this.interface_params = new ReactiveDict();

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
      name: 'interface/interface_params',
      messageType: 'rapid_turtlebot_msgs/InterfaceParams'
    });

    this.view_listener.subscribe(function(message) {
      that.interface_type.set(message.interface_type);
      that.interface_params = new ReactiveDict();
      for (var i=0; i<message.keys.length; i+=1) {
        var key = message.keys[i];
        var value = message.values[i];
        that.interface_params.set(key, value);
      }
    });

    this.view_publisher = new ROSLIB.Topic({
      ros: ros,
      name: 'interface/interface_submissions',
      messageType: 'rapid_turtlebot_msgs/InterfaceSubmissions'
    });
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
