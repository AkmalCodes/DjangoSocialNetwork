// Copyright 2023 HisyamPro
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Select the necessary elements
const createPostButton = document.getElementById("create-post");
const createPostsDiv = document.getElementById("create-posts");
const postsContainer = document.querySelector(".posts");

// Attach event listener to the create post button
createPostButton.addEventListener("click", createNewPost);

// Function to create a new post div
function createNewPost() {
  // Get the input values
  const postTitle = document.getElementById("create-postTitle").value;
  const postContent = document.getElementById("create-postContent").value;

  // Create the new post div
  const newPostDiv = document.createElement("div");
  newPostDiv.className = "posts-child";
  newPostDiv.innerHTML = `
                <!-- Code for the new post div -->
                <div class="posts-top">
                    <!-- Rest of the code -->
                </div>
                <div class="posts-title">
                    <p>${postTitle}</p>
                </div>
                <div class="reaction-bar">
                    <!-- Rest of the code -->
                </div>
                <div class="comment-display">
                    <!-- Rest of the code -->
                </div>
            `;

  // Insert the new post div into the posts container
  postsContainer.prepend(newPostDiv);

  // Clear the input fields
  document.getElementById("create-postTitle").value = "";
  document.getElementById("create-postContent").value = "";

  // Scroll to the newly created post
  newPostDiv.scrollIntoView();
}

document
  .getElementById("submit-comment")
  .addEventListener("click", function () {
    var main = document.querySelector("main");
    var commentText = document.getElementById("comment-textarea").value;

    // Create the comment container
    var comment = document.createElement("div");
    comment.setAttribute("id", "comment");

    // Create the top-comment container
    var topComment = document.createElement("div");
    topComment.setAttribute("id", "top-comment");

    // Create the comment-user-docreation-tocreation container
    var userCreation = document.createElement("div");
    userCreation.setAttribute("id", "comment-user-docreation-tocreation");

    // Create the img container
    var imgContainer = document.createElement("div");
    imgContainer.setAttribute("id", "img");

    // Create the img element
    var img = document.createElement("img");
    img.setAttribute("src", "resources/profile.png");
    img.setAttribute("width", "40px");
    img.setAttribute("height", "40px");

    // Append the img element to the img container
    imgContainer.appendChild(img);

    // Append the img container to the comment-user-docreation-tocreation container
    userCreation.appendChild(imgContainer);

    // Create the post-author paragraph
    var postAuthor = document.createElement("p");
    postAuthor.setAttribute("id", "post-author");
    postAuthor.innerHTML = 'created by <a href="#">username</a>';

    // Create the post-doc paragraph
    var postDoc = document.createElement("p");
    postDoc.setAttribute("id", "post-doc");
    postDoc.innerHTML = "date of creation";

    // Create the post-toc paragraph
    var postToc = document.createElement("p");
    postToc.setAttribute("id", "post-toc");
    postToc.innerHTML = "time of creation";

    // Append the paragraphs to the comment-user-docreation-tocreation container
    userCreation.appendChild(postAuthor);
    userCreation.appendChild(postDoc);
    userCreation.appendChild(postToc);

    // Append the comment-user-docreation-tocreation container to the top-comment container
    topComment.appendChild(userCreation);

    // Create the bottom-comment container
    var bottomComment = document.createElement("div");
    bottomComment.setAttribute("id", "bottom-comment");

    // Create the paragraph for the comment text
    var commentTextParagraph = document.createElement("p");
    commentTextParagraph.innerHTML = commentText;

    // Append the comment text paragraph to the bottom-comment container
    bottomComment.appendChild(commentTextParagraph);

    // Append the top-comment and bottom-comment containers to the comment container
    comment.appendChild(topComment);
    comment.appendChild(bottomComment);

    // Append the comment container to the main element
    main.appendChild(comment);
  });

// Get the comment button element
const commentButton = document.querySelector(
  ".reaction-bar button:first-of-type"
);

// Get the comment container element
const commentContainer = document.querySelector(".comment-display");

// Add a click event listener to the comment button
commentButton.addEventListener("click", () => {
  // Toggle the visibility of the comment container
  commentContainer.style.display =
    commentContainer.style.display === "none" ? "flex" : "none";
});
