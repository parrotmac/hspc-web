/**
 * Created by isaac on 8/7/17.
 */
var Hello = React.createClass({displayName: 'Hello',
    render: function() {
        return React.createElement("div", null, "Hello ", this.props.name);
    }
});

React.render(React.createElement(Hello, {name: "World"}), document.body);
