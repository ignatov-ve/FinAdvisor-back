import React from "react";
import PropTypes from "prop-types";

export default (props) => {
    return (
        <div>
            <p>{props.message}</p>
            <button onClick={props.closeMe}>Close Popup</button>
        </div>
    );
}