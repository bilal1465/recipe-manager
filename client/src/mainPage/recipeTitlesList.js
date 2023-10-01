import React from "react";

function RecipeTitlesList({data}) {
    const recipes = Object.values(data);
    

    return (
        <ul>
            {recipes.map((value, index) => (
                <li key={index}><div onClick={() => null}>{value}</div></li>
            ))}
        </ul>
    );
}

export default RecipeTitlesList;