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
        branch_coverage["fetch_brute_kddcup99_available"] = True
        try:
            X = joblib.load(samples_path)
            y = joblib.load(targets_path)
        except Exception as e:
            branch_coverage["fetch_brute_kddcup99_oserror"] = True
            raise OSError(
                "The cache for fetch_kddcup99 is invalid, please delete "
                f"{str(kddcup_dir)} and run the fetch_kddcup99 again"
            ) from e

    elif download_if_missing:
        branch_coverage["fetch_brute_kddcup99_download_if_missing"] = True
        _mkdirp(kddcup_dir)
        logger.info("Downloading %s" % archive.url)
        _fetch_remote(archive, dirname=kddcup_dir, n_retries=n_retries, delay=delay)
        DT = np.dtype(dt)
        logger.debug("extracting archive")
        archive_path = join(kddcup_dir, archive.filename)
        file_ = GzipFile(filename=archive_path, mode="r")
        Xy = []
        for line in file_.readlines():
            line = line.decode()
            Xy.append(line.replace("\n", "").split(","))
        file_.close()
        logger.debug("extraction done")
        os.remove(archive_path)

        Xy = np.asarray(Xy, dtype=object)
        for j in range(42):
            Xy[:, j] = Xy[:, j].astype(DT[j])

        X = Xy[:, :-1]
        y = Xy[:, -1]

        joblib.dump(X, samples_path, compress=0)
        joblib.dump(y, targets_path, compress=0)
    else:
        branch_coverage["fetch_brute_kddcup99_oserror"] = True
        raise OSError("Data not found and `download_if_missing` is False") >

<Provide a screenshot of the coverage results output by the instrumentation >

<Function 2 name : _fetch_kddcup99>

<Provide the same kind of information provided for Function 1
if subset == "SA":
        branch_coverage["fetch_kddcup99_subset_SA"] = True
        s = target == b"normal."
        t = np.logical_not(s)
        normal_samples = data[s, :]
        normal_targets = target[s]
        abnormal_samples = data[t, :]
        abnormal_targets = target[t]

        n_samples_abnormal = abnormal_samples.shape[0]
        random_state = check_random_state(random_state)
        r = random_state.randint(0, n_samples_abnormal, 3377)
        abnormal_samples = abnormal_samples[r]
        abnormal_targets = abnormal_targets[r]

        data = np.r_[normal_samples, abnormal_samples]
        target = np.r_[normal_targets, abnormal_targets]

    if subset in {"SF", "http", "smtp"}:
        branch_coverage["fetch_kddcup99_subset_SF_http_smtp"] = True
        s = data[:, 11] == 1
        data = np.c_[data[s, :11], data[s, 12:]]
        feature_names = feature_names[:11] + feature_names[12:]
        target = target[s]

        data[:, 0] = np.log((data[:, 0] + 0.1).astype(float, copy=False))
        data[:, 4] = np.log((data[:, 4] + 0.1).astype(float, copy=False))
        data[:, 5] = np.log((data[:, 5] + 0.1).astype(float, copy=False))

        if subset == "http":
            branch_coverage["fetch_kddcup99_subset_http"] = True
            s = data[:, 2] == b"http"
            data = data[s]
            target = target[s]
            data = np.c_[data[:, 0], data[:, 4], data[:, 5]]
            feature_names = [feature_names[0], feature_names[4], feature_names[5]]

        if subset == "smtp":
            branch_coverage["fetch_kddcup99_subset_smtp"] = True
            s = data[:, 2] == b"smtp"
            data = data[s]
            target = target[s]
            data = np.c_[data[:, 0], data[:, 4], data[:, 5]]
            feature_names = [feature_names[0], feature_names[4], feature_names[5]]

        if subset == "SF":
            data = np.c_[data[:, 0], data[:, 2], data[:, 4], data[:, 5]]
            feature_names = [
                feature_names[0],
                feature_names[2],
                feature_names[4],
                feature_names[5],
            ]

    if shuffle:
        branch_coverage["fetch_kddcup99_shuffle"] = True
        data, target = shuffle_method(data, target, random_state=random_state)

    fdescr = load_descr("kddcup99.rst")

    frame = None
    if as_frame:
        frame, data, target = _convert_data_dataframe(
            "fetch_kddcup99", data, target, feature_names, target_names
        )

    if return_X_y:
        branch_coverage["fetch_kddcup99_return_X_y"] = True
        return data, target>

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

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Team member 1: Stefanos Poullos>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test

def test_fetch_kddcup99_download_if_missing():
    with patch("sklearn.datasets._kddcup99.exists", return_value=False), \
         

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved

==> The coverage has improved because now we cover the case where dataset is not available locally by setting the flag to false in the patch
>

<Test 2>

<Provide the same kind of information provided for Test 1

patch("sklearn.datasets._kddcup99.GzipFile") as mock_gzipfile, \

mock_gzipfile.return_value.__enter__.return_value.readlines.return_value = [
            b"0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,511,511,0.00,0.00,0.00,0.00,0.00,0.00,0,0,1.00,0.00,0.00,0.00,0.00,0.00,normal.\n"
        ]
>
<State the coverage improvement with a number and elaborate on why the coverage is improved

==> The coverage has improved because by mocking the data we ensure that all code paths are tested, since some code paths are rarely executed in normal usage and in this case the network calls prevent that
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

