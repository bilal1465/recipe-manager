import React from "react";

function RecipeTitlesList({data}) {
    const recipes = Object.values(data);

    return (
        <ul>
            {recipes.map((value, index) => (
                <li key={index}>{value}</li>
            ))}
        </ul>
    );
}

export default RecipeTitlesList;