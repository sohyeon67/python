import { useState, useEffect } from 'react';
import './App.css';
import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import ReactHtmlParser from 'react-html-parser';
import Axios from 'axios';

function App() {
	const [vo, setEmp] = useState({
		e_id: '',
		e_name: '',
		gen: '',
		addr: ''
	})

	const [list, setList] = useState([]);

	//useEffect(() => {
	//	Axios.get('http://localhost:8000/api/get').then((response) => {
	//		console.log("useEffect response",response);
	//		setList(response.data);
	//	})
	//	console.log("useEffect");
	//}, [list])

	const insertEmp = () => {
		var e_id = document.querySelector("input[name='e_id']").value;
		var e_name = document.querySelector("input[name='e_name']").value;
		var gen = document.querySelector("input[name='gen']").value;
		var addr = document.querySelector("input[name='addr']").value;
		
		Axios.post('http://localhost:8000/emp/insert', {
			e_id: e_id,
			e_name: e_name,
			gen: gen,
			addr: addr,
		}).then((response) => {
			var cnt = response.data;
			if(cnt == 1) {
				refreshEmp();
				document.querySelector("input[name='e_id']").value = "";
				document.querySelector("input[name='e_name']").value = "";
				document.querySelector("input[name='gen']").value = "";
				document.querySelector("input[name='addr']").value = "";
			}
		})
	};
	
	const refreshEmp = () => {
		Axios.get('http://localhost:8000/emp/select_list').then((response) => {
			console.log("useEffect response",response);
			setList(response.data);
		})

	};
	
	const updateEmp = () => {
		console.log("updateEmp");
	};
	const deleteEmp = () => {
		console.log("deleteEmp");
	};
	const selectEmp = e => {
		var e_id = e.target.innerHTML;
		
		Axios.post('http://localhost:8000/emp/select_one', {
			e_id: e_id,
		}).then((response) => {
			var vo = response.data;
			console.log(vo);
			document.querySelector("input[name='e_id']").value = vo.e_id;
			document.querySelector("input[name='e_name']").value = vo.e_name;
			document.querySelector("input[name='gen']").value = vo.gen;
			document.querySelector("input[name='addr']").value = vo.addr;
		})
	};
	
	const getValue = e => {
		const { name, value } = e.target;
		console.log(name,value);
		console.log("before", vo);
		setEmp({
			...vo,
			[name]: value
		})
		console.log("after", vo);
	};
	
	


	return (
		<div className="App">
			<table border="1px">
				<thead>
					<tr>
						<td>사번</td>
						<td>이름</td>
						<td>성별</td>
						<td>주소</td>
					</tr>
				</thead>
			
				<tbody>
				{list.map(vo =>
					<tr key="{vo.e_id}">
						<td onClick={selectEmp}>{vo.e_id}</td>
						<td>{vo.e_name}</td>
						<td>{vo.gen}</td>
						<td>{vo.addr}</td>
					</tr>
				)}
				</tbody>
			</table>
			
			
			<table border="1px">
				<tbody>
					<tr>
						<td>사번</td>
						<td>
							<input type='text' onChange={getValue} name='e_id' />
						</td>
					</tr>
					<tr>
						<td>이름</td>
						<td>
							<input type='text' onChange={getValue} name='e_name' />
						</td>
					</tr>
					<tr>
						<td>성별</td>
						<td>
							<input type='text' onChange={getValue} name='gen' />
						</td>
					</tr>
					<tr>
						<td>주소</td>
						<td>
							<input type='text' onChange={getValue} name='addr' />
						</td>
					</tr>
					<tr>
						<td colSpan="2">
							<input type="button" value="추가" onClick={insertEmp} />
							<input type="button" value="수정" onClick={updateEmp} />
							<input type="button" value="삭제" onClick={deleteEmp} />
							<input type="button" value="갱신" onClick={refreshEmp} />
						</td>
					</tr>
					
					
				</tbody>
			</table>

		</div>
	);
}

export default App;
