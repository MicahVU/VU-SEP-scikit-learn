# Report for Assignment 1

## Project chosen

Name: scikit-learn

URL: https://github.com/scikit-learn/scikit-learn

Number of lines of code and the tool used to count it: 268.052

Programming language: Python(92,4%), Cython(5,6%), C++(1,1%), Meson(0,2%), Shell(0,3%), C(0,1%)

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>
Python, coverage.py (pytest)

<Show the coverage results provided by the existing tool with a screenshot>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Team member 1: Stefanos Poullos>

<Function 1 name : def _fetch_brute_kddcup99>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements
if available:
(https://github.com/MicahVU/VU-SEP-scikit-learn/commit/c783cbcf466b43095be9945aa2496a4387b6042e#diff-6020384f05da59b3ef5b9078a33ceca19b61f65b7b18806c9b91587fd22594e0)>

<Provide a screenshot of the coverage results output by the instrumentation
 (https://github.com/MicahVU/VU-SEP-scikit-learn/blob/main/coverage_of_functions_before_instrumentation.jpg) >

<Function 2 name : _fetch_kddcup99>

<Provide the same kind of information provided for Function 1

these are the same links as above since both functions were done in the same commit

(https://github.com/MicahVU/VU-SEP-scikit-learn/commit/c783cbcf466b43095be9945aa2496a4387b6042e#diff-6020384f05da59b3ef5b9078a33ceca19b61f65b7b18806c9b91587fd22594e0)


(https://github.com/MicahVU/VU-SEP-scikit-learn/blob/main/coverage_of_functions_before_instrumentation.jpg)
>

<Team member 2: Yevgeniy Stadnyk>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

<Team member 3: Mikolaj Magiera>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

<Team member 4: Micah Rouwendaal>

<Function 1 name>
def _extract_patches(arr, patch_shape=8, extraction_step=1)

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/MicahVU/VU-SEP-scikit-learn/commit/fc9299bc946944e9a6b505bad1cfa899ec25be24

<Provide a screenshot of the coverage results output by the instrumentation>
<img src="assignment1_images/branchcov_image_extract_patches.PNG">

<Function 2 name>
def _compute_n_patches(i_h, i_w, p_h, p_w, max_patches=None)

<Provide the same kind of information provided for Function 1>
<Link to commit made in forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/MicahVU/VU-SEP-scikit-learn/commit/0853288f57f631c83d082cbe57c952b0c63238aa

<Provide a screenshot of the coverage results output by the instrumentation>
<img src="assignment1_images/branchcov_image_compute_n_patches.PNG">


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Team member 1: Stefanos Poullos>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test

(https://github.com/MicahVU/VU-SEP-scikit-learn/commit/c783cbcf466b43095be9945aa2496a4387b6042e#diff-d75de98f144d7a70bd99b7359f0fa9420a0229ba6800d1d7624d5e2e2209babe)


<Provide a screenshot of the old coverage results (the same as you already showed above)>
(https://github.com/MicahVU/VU-SEP-scikit-learn/blob/main/coverage_of_functions_before_instrumentation.jpg)

<Provide a screenshot of the new coverage results>
(https://github.com/MicahVU/VU-SEP-scikit-learn/blob/main/coverage_of_functions_after_instrumentation.jpg)
(https://github.com/MicahVU/VU-SEP-scikit-learn/blob/main/coverage_of_test_file_after.jpg)

<State the coverage improvement with a number and elaborate on why the coverage is improved
(number is in the second explanation)

==> The coverage has improved because now we cover the case where dataset is not available locally by setting the flag to false in the patch
>

<Test 2>

<Provide the same kind of information provided for Test 1
The  links are exactly the same because the tests have been improved in the same commit
>
<State the coverage improvement with a number and elaborate on why the coverage is improved

==> The coverage has improved (26% -> 98%) because by mocking the data we ensure that all code paths are tested, since some code paths are rarely executed in normal usage and in this case the network calls prevent that
>
<Team member 2: Yevgeniy Stadnyk>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

<Team member 3: Mikolaj Magiera>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

<Team member 4: Micah Rouwendaal>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

