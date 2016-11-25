import Menu, {SubMenu, MenuItem} from 'rc-menu';
ReactDOM.render(<Menu>
  <MenuItem>1</MenuItem>
  <SubMenu title="2">
  <MenuItem>2-1</MenuItem>
  </SubMenu>
</Menu>, container);

